build : interpose.so

interpose.so : interpose.c
	gcc -shared -ldl -fPIC -fno-builtin -o interpose.so interpose.c

.PHONY : build random run perftest

random : gen_interpose.py
	./gen_interpose.py $(MAX_DELAY)
	make interpose.so

run : build
	LD_PRELOAD=$(PWD)/interpose.so ./fuzz.py

perftest : perftest.py
	LD_PRELOAD=$(PWD)/interpose.so ./perftest.py
