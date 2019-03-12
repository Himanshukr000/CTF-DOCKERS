#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h> // for open
#include <unistd.h> // for close

int devrand = -1;
int nextind = 0;
int cans[10];
char *password;
#define BUFSIZE 40
#define PASSIZE 32

// All allocated on stack
typedef struct {
    // The data
    char buf[BUFSIZE];
    // Randomly generated Stack-Canary Value
    int can;
    // The index in cans[]
    int index;
} Canary;

void initCanary(Canary *c) {
    // Clear any data
    memset(c, 0, BUFSIZE);
    // init canary value
    read(devrand, &c->can, sizeof(int));
    // mark the index in the list
    c->index = nextind;
    // store the .data value
    cans[nextind] = c->can;
    // increment next-index value
    nextind++;
}

void checkCanary(Canary *c) {
    // get possibly-overwritten value
    int a = c->can;
    // get expected value
    int b = cans[c->index];
    if (a != b) {
	puts("---------------------- HEY NO STACK SMASHING! --------------------");
	exit(1);
    }
}

void checkPass(char *pass, char *buf) {
    // Check if they are right
    if (!memcmp(pass, buf, PASSIZE)) {
	puts("*unlocks door*\nYou're cool, c'mon in");
	system("/bin/cat ./flag");
	/*
	printf("Whatya have? ");
	char *buf = malloc(50);
	read(0, buf, 50);
	printf(buf);
	printf("That's strong stuff. If you say so...\n");
	*/
    } else {
	puts("Yeah right! Scram");
    }
}

void doCanary(Canary *c) {
    //	Create Stack Canary & Buffer
    initCanary(c);

    // Get input
    read(0, c->buf, 420);
    //puts("Canary not checked...");
    checkCanary(c);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 20);
    setvbuf(stdin, NULL, _IONBF, 20);
    devrand  = open("/dev/urandom", 0);
    password = malloc(PASSIZE);

    // Get input for password
    printf("*slides open window*\nPassword? ");
    // Init/do canary stuff
    Canary c[1]; // <-- Because I'm retarted
    doCanary(c);

    // Read in password data
    int pfd = open("./password", 0);
    read(pfd, password, PASSIZE+1);

    checkPass(password, c->buf);

    return 0;
}
