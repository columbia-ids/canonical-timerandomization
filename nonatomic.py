#!/usr/bin/env python

import threading, time

# approximately half of the time required to complete the operations
# encoded by the statement (x+=1) on the test system
HALF=2.8e-05
# the global variable
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
	count = 0
	while(True):
		if(abs(x)>1):
			x = 5
			break
		count += 1
		time.sleep(HALF)
		x += 1
		l.acquire()
		x -= 1
		l.release()
	print str(count) + ' loops required to fuzz xplusplus.'

lock = threading.Lock()
t1 = threading.Thread(target=xplusplus, args=(lock,))
t2 = threading.Thread(target=fuzzer, args=(lock,))
t1.start()
t2.start()
t2.join()
t1.join()
