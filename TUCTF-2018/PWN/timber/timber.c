#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h> // for open
#include <unistd.h> // for close
#include <time.h> // time...

int tage;
char *ttype;
int devrand;

// Win function (not called)
void date() {
    system("/bin/cat ./flag");
}

void getName(char *buf) {
    printf("Welcome to Timber™!\nThe world's largest lumberjack dating site\nPlease enter your name: ");
    memset(buf, 0, 24);
    read(0, buf, 100);
}

void clearStdin() {
    char c; while ((c = getchar()) != '\n' && c != EOF){} // Clearing stdin
}

// Generates a random value from 0-max
int getRand(int max) {
    unsigned int rand = 0;
    read(devrand, &rand, sizeof(int));
    rand = rand % max;
    return rand;
}

// Generates a tree type and age
void genMatch() {
    // Random age
    tage = getRand(5000);
    // Random value in range 0-10 to decide tree type
    int type = getRand(10);
    switch (type) {
	case 0:
	    ttype = "Sugar Maple"; break;
	case 1:
	    ttype = "Bonsai"; break;
	case 2:
	    ttype = "American Beech"; break;
	case 3:
	    ttype = "American Elm"; break;
	case 4:
	    ttype = "Black Cherry"; break;
	case 5:
	    ttype = "American sycamore"; break;
	case 6:
	    ttype = "White Spruce"; break;
	case 7:
	    ttype = "Eastern Pine"; break;
	case 8:
	    ttype = "Northern Oak"; break;
	case 9:
	    ttype = "Shagbark Hickory"; break;
	case 10:
	    ttype = "Swamp Birch"; break;
	default:
	    ttype = "Unkown"; break;
    }
}

// the actual program
void doStuff() {
    // Get name & leak canary
    char uname[24];
    getName(uname);
    printf("Alright "); printf(uname);
    puts("Let's find you a match!");
    puts("Options:\n l: Swipe Left\n r: Swipe Right\n s: Super Swipe\n");

    // For fun
    while (1) {
	genMatch();
	printf("%s age %d? ", ttype, tage);
	// Swipe Input
	char c;
	scanf("%c", &c);
	clearStdin();
	// Random chance for a match, or gurantee
	if (c == 'r' && !getRand(10) || c == 's') {
	    puts("+Match Found!");
	    printf("----------------- %s ----------------\n", ttype);
	    printf("[%s] So, are you a tree hugger or what.\n", ttype);
	    char buf[48];
	    read(0, buf, 100);
	    printf("[%s] Pff, lumberjacks are all the same.\n", ttype);
	    break;
	}
    }
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 20);
    setvbuf(stdin, NULL, _IONBF, 20);
    devrand = open("/dev/urandom", 0);

    // The actual program
    doStuff();

    close(devrand);
    return 0;
}
