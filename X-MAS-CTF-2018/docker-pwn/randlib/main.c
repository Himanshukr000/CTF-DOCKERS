#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    char buffer[32];
    puts("This is easier than you would think...");
    puts("Santa allowed you to ROP me!");

    gets(buffer);

    return 0;
}
