#!/usr/bin/env python

import threading, time, datetime

# approximately half of the time required to complete the operations
# encoded by the statement (x+=1) on the test system
STEP=2.8e-06
# the global variable
x=0

def xplusplus(l):
	global x
	count1 = 0
	t1 = datetime.datetime.now()
	while(True):
		if(abs(x)>1):
			x = 5
			break
		count1 += 1
		x += 1
		l.acquire()
		x -= 1
		l.release()
	t2 = datetime.datetime.now()
	print 'One loop time: ' + str((t2-t1).total_seconds()/count1) + '\n'

def fuzzer(l):
	global x
	count2 = 0
	while(True):
		if(abs(x)>1):
			x = 5
			break
		count2 += 1
		time.sleep(STEP)
		x += 1
		l.acquire()
		x -= 1
		l.release()
	print str(count2) + ' loops required to fuzz xplusplus.'

lock = threading.Lock()
t1 = threading.Thread(target=xplusplus, args=(lock,))
t2 = threading.Thread(target=fuzzer, args=(lock,))
t1.start()
t2.start()
t2.join()
t1.join()
