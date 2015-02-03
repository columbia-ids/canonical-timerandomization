#!/usr/bin/env python

import threading, Queue, time, datetime

x=0

def xplusplus(l):
	global x
	count = 0
	while(True):
		if(abs(x)>1):
			x = 5
			break
		count += 1
		x += 1
		l.acquire()
		x -= 1
		l.release()

def fuzzer(l):
	global x
	res = datetime.timedelta.resolution.total_seconds()
	half = 2.8e-05
	count = 0
	while(True):
		if(abs(x)>1):
			x = 5
			break
		count += 1
		time.sleep(half)
		x += 1
		l.acquire()
		x -= 1
		l.release()
	print str(count) + ' loops required to fuzz xplusplus.'

threads = list()
lock = threading.Lock()
queue = Queue.Queue()
t1 = threading.Thread(target=xplusplus, args=(lock,))
t2 = threading.Thread(target=fuzzer, args=(lock,))
t1.start()
t2.start()
t2.join()
t1.join()
