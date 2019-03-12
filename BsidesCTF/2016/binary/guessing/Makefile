# enable all warnings
CFLAGS += -Wall

# x86
CFLAGS += -m32

guessing: guessing.c
	# NX-disable
	$(CC) $(CFLAGS)	-z execstack $< -o $@

guessing2: guessing.c
	$(CC) $(CFLAGS)	$< -o $@

all: guessing guessing2

clean:
	rm -f guessing guessing2
