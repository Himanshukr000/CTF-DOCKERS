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

    int len = 21;
    char *str = malloc(len+1);
    memset(str, 0, len+1);
    printf("Gimme that good stuff: ");
    read(0, str, len);
    printf("%s\n", str);
    char *tmp = malloc(len);

    // Letter shift
    // 0123456789
    // 7890123456
    for (int i = 0; i < len; i++) {
	int x = (i+(len-10)) % len;
	tmp[i] = str[x];
    }
    memcpy(str, tmp, len);
    printf("%s\n", str);


    // add a dad dad
    for (int i = 0; i < len; i++) {
	char c = str[i];
	char z = c + 5;
	str[i] = z;
    }
    printf("%s\n", str);


    // Reverse string
    for (int i = len-1; i >= 0; i--) {
	tmp[len-i-1] = str[i];
    }
    memcpy(str, tmp, len);
    printf("%s\n", str);


    return 0;
}
