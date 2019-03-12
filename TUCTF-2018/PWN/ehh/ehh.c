#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h> // for open
#include <unistd.h> // for close
#include <time.h> // time...

// Value in .data to change
int val = 0xbaadaa55;

int main() {
    setvbuf(stdout, NULL, _IONBF, 20);
    setvbuf(stdin, NULL, _IONBF, 20);

    char buf[24];
    printf(">Input interesting text here< %p\n", &val);

    read(0, buf, 24);
    // %n overwrite
    printf(buf);

    if (val == 24)
	system("/bin/cat ./flag");

    return 0;
}
