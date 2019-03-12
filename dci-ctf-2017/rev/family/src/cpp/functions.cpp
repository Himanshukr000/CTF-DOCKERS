#include "../hpp/functions.hpp"

void gen_random(char *s, const int len)
{
    static const char alphanum[] =
        "0123456789"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz";

    for (int i = 0; i < len; ++i)
    {
        s[i] = alphanum[rand() % (sizeof(alphanum) - 1)];
    }

    s[len] = 0;
}

void xor_string(char* txt, char* key, int txtlen)
{
    int keylen = strlen(key);
    int i = 0, j = 0;

    for (i = 0; i < txtlen; ++i, j = (j+1)%keylen)
    {
        txt[i] = txt[i] ^ key[j];
    }
}

void create_xored_data(char* txt, char* key, ofstream& output)
{
    int txtlen = strlen(txt)+1;
    int i = 0;

    xor_string(txt, key, txtlen);

    output << "char msg[] = {";
    for (i = 0; i < txtlen; i++) {
        if (i != 0)
            output << ", ";
        output << to_string((int)txt[i]);
    }
    output << ", 0};" << std::endl;
}