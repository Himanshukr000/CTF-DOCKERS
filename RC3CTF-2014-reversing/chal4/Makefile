CFLAGS=-std=c99 -DCTF_THREADS -DCTF_SPEC
CC=gcc
CLIBFLAGS=-lpthread
CSOURCE=ctfserver.c chal4.c

all: chal4

chal4: clean
	$(CC) $(CFLAGS) -o chal4 $(CSOURCE) $(CLIBFLAGS)

debug: clean
	$(CC) $(CFLAGS) -o chal4 -ggdb $(CSOURCE) $(CLIBFLAGS)

clean:
	rm -rf chal4
