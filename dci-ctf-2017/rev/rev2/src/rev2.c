#include <stdio.h>
#include <string.h>


void xor_string(char* txt, char* key, int txtlen)
{
    int keylen = strlen(key);
    int i = 0, j = 0;

    for (i = 0; i < txtlen; ++i, j = (j+1)%keylen)
    {
        txt[i] = txt[i] ^ key[j];
    }
}

/*
// flag used to generate the cipher text:
char flag[] = "DCI{+_Plain-Text_Passwords-FTW_}";

void create_xored_data(char* txt, char* key)
{
    int txtlen = strlen(txt);
    int i = 0;

    xor_string(txt, key, txtlen);

    printf("char data[] = {");
    for (i = 0; i < txtlen; i++) {
        if (i != 0)
            printf(", ");
        printf("%d", txt[i]);
    }
    printf("};\n");
}
*/


int main()
{
    char key[]    = "17EiD6hgboZpoUlvMFHciPI1J62ZDNyo";
    char hidden[] = {
        117, 116, 12, 18, 111, 105, 56, 11, 3, 6, 52, 93, 59, 48, 20, 2, 18,
        22, 41, 16, 26, 39, 38, 67, 46, 69, 31, 28, 16, 25, 38, 18, 0
    };
    char input[32];
    char *pos;

    puts("\nThis time the flag is hidden and protected by a password!");
    puts("Only those who have the right password can access the flag.\n");
    printf("Password: ");

    fgets(input, sizeof(input), stdin);
    if ((pos = strchr(input, '\n')) != NULL)
    {
        *pos = '\0';
    }

    if (strcmp(input, "02jKcfHaMCDKCoki") == 0)
    {
        xor_string(hidden, key, sizeof(hidden)-1);
        printf("%s\n\n", hidden);
    }
    else
    {
        printf("Wrong password!\n\n");
    }

    return 1;
}