#!/usr/bin/env python

import threading, Queue

x=0

def xplusplus(l, q):
	global x
	while(abs(x)<=1):
		l.acquire()
		x += 1
		l.release()
		l.acquire()
		x -= 1
		l.release()
	q.put(x)

threads = list()
lock = threading.Lock()
queue = Queue.Queue()
for i in range(2):
	threads.append(threading.Thread(target=xplusplus, args=(lock, queue)))
	threads[i].daemon = True
	threads[i].start()
print queue.get()
