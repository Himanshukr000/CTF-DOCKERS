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
char txt[] = "Wow! You acutally saved Timmy. You are a true hero... As a "
             "reward, not only will Timmy\ngive you his flag, but he will "
             "also give you an hint for the challenge called \"tinyelf\":\n\n"
             "The challenge was greatly inspired by this tutorial:\n"
             "http://www.muppetlabs.com/~breadbox/software/tiny/teensy.html";

void create_xored_data(char* txt, char* key)
{
    int txtlen = strlen(txt);
    int i = 0;

    xor_string(txt, key, txtlen);

    printf("char* data = {");
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
    char key[] = "NqTaxv65ky0S73LDn1agWhA7ksx8tPDo";
    char hidden[] = {25, 30, 35, 64, 88, 47, 89, 64, 75, 24, 83, 38, 67, 82, 32,
        40, 23, 17, 18, 6, 33, 13, 37, 23, 63, 26, 21, 85, 13, 126, 100, 54,
        33, 4, 116, 0, 10, 19, 22, 84, 75, 13, 66, 38, 82, 19, 36, 33, 28, 94,
        79, 73, 121, 72, 0, 68, 75, 18, 88, 74, 17, 39, 37, 29, 42, 93, 116,
        15, 23, 2, 22, 90, 5, 21, 73, 115, 64, 90, 32, 40, 78, 101, 8, 10, 58,
        17, 75, 80, 2, 5, 29, 24, 13, 63, 49, 79, 38, 24, 39, 65, 30, 26, 87,
        82, 71, 89, 82, 38, 67, 19, 36, 33, 78, 70, 8, 11, 59, 72, 32, 91, 24,
        28, 88, 95, 29, 38, 33, 79, 55, 30, 33, 65, 25, 24, 22, 93, 2, 23, 68,
        115, 81, 92, 62, 100, 26, 89, 4, 71, 52, 0, 32, 91, 7, 22, 22, 95, 17,
        112, 39, 14, 34, 29, 49, 5, 88, 84, 66, 92, 5, 0, 85, 63, 81, 17, 118,
        78, 100, 101, 9, 2, 119, 11, 41, 86, 7, 31, 29, 86, 19, 53, 100, 24, 47,
        2, 116, 6, 10, 19, 87, 65, 7, 0, 16, 58, 89, 64, 60, 45, 28, 84, 5, 71,
        53, 17, 97, 67, 3, 26, 11, 24, 0, 37, 48, 0, 60, 24, 53, 13, 66, 124,
        94, 65, 31, 9, 10, 124, 24, 68, 59, 51, 64, 92, 20, 23, 39, 13, 53, 91,
        10, 17, 11, 22, 23, 63, 41, 64, 48, 19, 38, 4, 25, 18, 84, 90, 19, 86,
        67, 60, 81, 71, 59, 37, 28, 84, 78, 19, 62, 6, 56, 24, 31, 22, 29, 86,
        7, 41, 106, 7, 58, 28, 56, 0
    };

	puts("\nThis nice little elf named Timmy is about to give you a flag!");
    puts("Sadly, on its way to you it crashes... ");
    puts("The friendly elf is about to die a painful death :(\n");
    puts("Can you patch him up and save him?");
    puts("Or will you simply take the flag from its cold dead hands...?\n");
    puts("The choice is yours.\n");

    int num = 10;
	int denum = 0;
	int crash = num/denum; // division by zero, oh no!

    xor_string(hidden, key, sizeof(hidden)-1);
    printf("%s\n\n", hidden);

	puts("DCI{Shame-On-You_if_Timmy_died.}\n");

	return 1;
}