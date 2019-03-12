#include <stdio.h>
#include <unistd.h>

int main() {
    char buf[16];
    read(0, buf, 30);
    return 0;
}

void giveShell() {
    // The last 2 nops are replaced with: 0xa144 to screw with the interpretation of the instructions
    asm("nop\nnop\nnop");
    execve("/bin/sh", 0, 0);
}
