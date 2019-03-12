#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h> // for open
#include <unistd.h> // for close
#include <time.h> // time...

char *pass = "7h3_m057_53cr37357_p455w0rd_y0u_3v3r_54w";

int main() {
    setvbuf(stdout, NULL, _IONBF, 20);
    setvbuf(stdin, NULL, _IONBF, 20);

    char *buf = malloc(64);
    printf("*Ahem*... password? ");
    read(0, buf, 64);
    
    if (memcmp(buf, pass, 40)) {
	puts("yeahright!");
	exit(0);
    }

    system("/bin/cat ./flag");

    return 0;
}
