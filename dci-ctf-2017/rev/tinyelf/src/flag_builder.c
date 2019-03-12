#include <stdio.h>

int main()
{
    char buffer[128];
    char flag[32] = "DCI{To0oM4ny0pt1miz4t1onsKi1lsU}";
    FILE* fp;

    fp = fopen("tinyelf", "r");
    fread(buffer, 128, 1, fp);

    int i;
    char c = 0;
    char ans = 0;
    for (i = 0; i < 32; i++) {
        c = 0;
        if (i != 10) {
            c = buffer[i];
        }
        c += buffer[i+32];
        c += buffer[i+64];
        ans = flag[i] - c;
        
        /*
        printf("1: 0x%02x\n", buffer[i] & 0xFF);
        printf("2: 0x%02x\n", buffer[i+32] & 0xFF);
        printf("3: 0x%02x\n", buffer[i+64] & 0xFF);
        printf("4: 0x%02x\n", buffer[i+96] & 0xFF);
        printf("c: 0x%02x\n", c & 0xFF);
        printf("f: 0x%02x\n", flag[i] & 0xFF);
        printf("a: 0x%02x\n\n", ans & 0xFF);
        */

        printf("            db      0x%02x                            ; flag byte\n", ans & 0xFF);
    }
}

/*
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte
            db      0x00                            ; free byte

            db      0xfa                            ; flag byte
            db      0x05                            ; flag byte
            db      0x2a                            ; flag byte
            db      0xd0                            ; flag byte
            db      0x51                            ; flag byte
            db      0xeb                            ; flag byte
            db      0xa6                            ; flag byte
            db      0xbd                            ; flag byte
            db      0x60                            ; flag byte
            db      0x7d                            ; flag byte
            db      0x6c                            ; flag byte
            db      0x01                            ; flag byte
            db      0x25                            ; flag byte
            db      0x13                            ; flag byte
            db      0x67                            ; flag byte
            db      0xbc                            ; flag byte
            db      0xae                            ; flag byte
            db      0xfe                            ; flag byte
            db      0x14                            ; flag byte
            db      0x69                            ; flag byte
            db      0x91                            ; flag byte
            db      0x86                            ; flag byte
            db      0x02                            ; flag byte
            db      0x06                            ; flag byte
            db      0x2d                            ; flag byte
            db      0xf5                            ; flag byte
            db      0x2f                            ; flag byte
            db      0x6f                            ; flag byte
            db      0x3b                            ; flag byte
            db      0xf3                            ; flag byte
            db      0x75                            ; flag byte
            db      0x7c                            ; flag byte
*/