CSOURCE=chal5.c
CFLAGS=-std=c99
CC=gcc

all: static

chal5: clean
	$(CC) $(CFLAGS) -o chal5 $(CSOURCE)

debug: clean
	$(CC) $(CFLAGS) -o chal5 -ggdb $(CSOURCE)

static: clean
	$(CC) $(CFLAGS) -static -o chal5 $(CSOURCE)

clean:
	rm -rf chal5
