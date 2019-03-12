CC=gcc
CFLAGS=-std=c99 -DCTF_SPEC -DCTF_THREADS
CLIBFLAGS=-lpthread
CSOURCE=chal2.c ctfserver.c

all: static

chal2: clean
	$(CC) $(CFLAGS) -o chal2 $(CSOURCE) $(CLIBFLAGS)

debug: clean
	$(CC) $(CFLAGS) -o chal2 -ggdb $(CSOURCE) $(CLIBFLAGS)

static: clean
	$(CC) $(CFLAGS) -o chal2 -static $(CSOURCE) $(CLIBFLAGS)

clean:
	rm -rf chal2
