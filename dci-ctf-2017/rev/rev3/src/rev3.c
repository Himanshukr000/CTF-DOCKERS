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
// text used to generate the cipher text:
char flag[] = "DCI{One-Time-pad-and-a-key=easy}";

void create_xored_data(char* txt, char* key)
{
    int txtlen = strlen(txt)+1;
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
    char key[]    = "Gw1lg8kVnkMGf2SrQAF2oTbi4ChcFquKg";
    char input[64];
    char target[] = {
        3, 52, 120, 23, 40, 86, 14, 123, 58, 2, 32, 34, 75, 66, 50, 22, 124,
        32, 40, 86, 66, 53, 79, 2, 81, 58, 85, 6, 39, 2, 12, 54, 103
    };
    char* pos;
    int i = 0;

    printf("\nWe realized plain-text passwords were not safe, so we no longer\n"
           "use them. Instead, we decided to use the flag as the password!!\n\n");
    printf("Password: ");

    fgets(input, sizeof(input), stdin);
    if ((pos = strchr(input, '\n')) != NULL)
    {
        *pos = '\0';
    }

    for (i = 0; i < sizeof(target); ++i)
    {
        if ((input[i] ^ key[i]) != target[i])
        {
            puts("Wrong password!\n");
            return 0;
        }
    }

    puts("Success!\n");

    return 1;
}
