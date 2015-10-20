#coding=utf-8
__author__ = 'wb-zhangjinzhong'

import sqlite3

cx = sqlite3.connect("data/test.db")

cu = cx.cursor()

cu.execute("insert into t(name) values('a')")

cx.commit()

cu.close()
cx.close()

