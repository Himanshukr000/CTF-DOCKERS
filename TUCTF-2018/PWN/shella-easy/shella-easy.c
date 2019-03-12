#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h> // for open
#include <unistd.h> // for close
#include <time.h> // time...


int main() {
    setvbuf(stdout, NULL, _IONBF, 20);
    setvbuf(stdin, NULL, _IONBF, 20);

    int x = 0xcafebabe;
    char buf[64];
    printf("Yeah I'll have a %p with a side of fries thanks\n", buf);
    gets(buf);
    if (x != 0xdeadbeef)
	exit(0);

    return 0;
}
