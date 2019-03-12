#include <stdio.h>
#include <errno.h>
#include <string.h>

int main()
{
    struct {
        char input[32];
        int target;
    } locals;

    setbuf(stdout, NULL);

    locals.target = 0xBAD;
    printf("Enter an input: ");
    fgets(locals.input, 64, stdin);

    if (locals.target == 0xDEADBEEF) {
        FILE *file;
        file = fopen("/home/buf2/flag", "r");
        if (file) {
            fread(locals.input, 1, 32, file);
            fclose(file);
            puts("Congrats you got the flag: ");
            printf("%.32s\n", locals.input);
        } else {
            printf("fopen error: %d (%s)\n", errno, strerror(errno));
        }
    } else if (locals.target != 0xBAD) {
        printf("There was a buffer overflow, but the new value is incorrect.\n");
    } else {
        printf("There was no buffer overflow.\n");
    }
}
