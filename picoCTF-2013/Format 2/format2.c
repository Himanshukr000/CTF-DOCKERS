#undef _FORTIFY_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void be_nice_to_people() {
    // /bin/sh is usually symlinked to bash, which usually drops privs. Make
    // sure we don't drop privs if we exec bash, (ie if we call system()).
    gid_t gid = getegid();
    setresgid(gid, gid, gid);
}

int main(int argc, const char **argv) {
    be_nice_to_people();
    char buf[80];
    snprintf(buf, 70, argv[1]);
    printf(buf);
    printf("\n");
    system("/bin/ls");
    exit(0);
}
