#!/usr/bin/env python

import sys, datetime

if len(sys.argv) > 1: iterations = int(sys.argv[1])
else: iterations = 10000000

x = 0
t1 = datetime.datetime.now()
for i in range(iterations):
	x += 1
t2 = datetime.datetime.now()
print str((t2-t1).total_seconds()/iterations) + ' seconds per increment averaged over ' + str(iterations) + ' increments.'
