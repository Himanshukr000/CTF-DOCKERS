#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int pass = 0; // init  

void give_shell() // shell spawner
{
    gid_t gid = getegid(); //preserveid
    setresgid(gid, gid, gid);
    system("/bin/sh");
}

int main(int argc, char **argv)
{
    char buf[128];
    memset(buf, 0, sizeof(buf));
    printf("Here is the fuckup your ordered\n");
    fgets(buf, 128, stdin);
    printf(buf);
    if (pass == 1337)
    {
        give_shell();
    }
    else
    {
        printf("Nope.be smart|be elite.  %d\n", pass);
    }

    return 0;
}
