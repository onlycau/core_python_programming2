#!/usr/bin/env python3
# -*-coding:utf-8 -*-


import time
import pymysql


class My_mysql(object):

    def __init__(self):
        self.host = 'host'
        self.user = 'user_system'
        self.password = 'password'
        self.db = 'user_system'
        self.table = 'users'
        self.charset = 'utf8'
        self.cursor = self.cursor()

    def cursor(self):

        cursor = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, charset=self.charset).cursor()
        return cursor

    def is_user_in(self, name):
        sql = 'select * from %s where name=%s' % (self.table, name)
        return self.cursor.execute(sql)

    def is_password_right(self, name, password):
        sql = 'select password where name =%s' % name
        self.cursor.execute(sql)
        return bool(self.cursor.fetchone()[0] == password)


class Interface(object):

    def __init__(self):
        self.time = time()

    def sign_in(self, name, password):
        pass

    def sigin_up(self, name, password):
        pass


