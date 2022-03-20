#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: WireProgramLock.py
@Time    : 2022/3/20 18:10
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 线程锁Demo
"""

from threading import Thread, Lock

n = 5000

lock = Lock()


def f1():
	global n
	for i in range(100000):
		lock.acquire()
		n += 1
		lock.release()


def f2():
	global n
	for i in range(100000):
		lock.acquire()
		n -= 1
		lock.release()


t1 = Thread(target=f1)
t1.start()

t2 = Thread(target=f2)
t2.start()

t1.join()
t2.join()

print(n)
