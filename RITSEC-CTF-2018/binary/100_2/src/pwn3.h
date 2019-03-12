#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

static void myGets(char *buffer) {
    read(0, buffer, 0x1337);
}

static void myPrint(char *buffer) {
    printf("%s", buffer);
}

static void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
}