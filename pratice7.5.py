#!/usr/bin/env python3


import time
import os


class login(object):

    def __init__(self):

        self.users = self.users_get()

    def users_get(self):

        with open('names', 'r') as f:
            names = []
            for line in f:
                names.append(line.strip())
        with open('passwords', 'r') as f:
            passwords = []
            for line in f:
                passwords.append(line.strip())
        return dict(zip(names, passwords))

    def new_usr(self):

        username = ''
        password_1 = ''
        while True:
            username = input('please enter a name').lower()
            if not self.users.get(username):
                break
            username = input('username have been created.').lower()
        while True:
            password_1 = input('please enter your password:').lower()
            password_2 = input('please enter your password again:').lower()
            if password_1 == password_2:
                break
            else:
                print('different password, please try again.')
        with open('names', 'a+') as f:
            f.write(os.linesep + username)
        with open('passwords', 'a+') as f:
            f.write(os.linesep + password_1)
        print('name:%s/n password:%s succede new user.' % (username, password_1))

    def old_usr(self, username):

        while True:
            password = input('enter your password:').lower()
            if self.users.get(username) == password:
                print('login succeded.')
                return True
            else:
                print('wrong  password')

    def time_log():
        pass

    def new_or_old(self):
        while True:
            usr = input('please enter your user name:').lower()
            if usr == 'onlycau':
                self.administraition()
            elif usr in self.users:
                return usr
            else:
                q = input('are you a new user?(y or n)').lower()
                if q == 'y':
                    return False
                else:
                    print("it'a wrong username")

    def administraition(self):
        pass


def test():

    ob = login()
    usr = ob.new_or_old()
    if usr:
        ob.old_usr(usr)
    else:
        ob.new_usr()


if __name__ == '__main__':

    test()
