// gcc -fno-stack-protector -z execstack buf3.c -o buf3
#include <stdio.h>

int main()
{
    char input[32];

    setbuf(stdout, NULL);

    printf("Your input is at: %p\n", &input[0]);
    fgets(input, 64, stdin);

    printf("Your input is: %s\n", input);
}
