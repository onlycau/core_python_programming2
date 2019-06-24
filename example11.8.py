#!usr/bin/env python3


from time import time


def logged(when):

    def log(f, *args, **kargs):
        print('called:\n function:%s\nargs:%r\n kargs:%r' % (f, args, kargs))

    def pre_logged(f):
        def wrapper(*args, **kargs):
            log(f, *args, **kargs)
            return f(*args, **kargs)
        return wrapper

    def post_logged(f):
        def wrappered(*args, **kargs):
            now = time()
            try:
                return f(*args, **kargs)
            finally:
                log(f, *args, **kargs)
                print('time delta:%s' % (time() - now))
        return wrappered

    try:
        return{'pre': pre_logged, 'post': post_logged}[when]
    except KeyError as e:
        raise ValueError(e)


@logged("post")
def hello(name):
    print('hello', name)


hello('world')
