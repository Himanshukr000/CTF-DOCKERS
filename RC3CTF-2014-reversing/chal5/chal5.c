#include <stdio.h>

int RC3_ROOT_1776;
void RC3_NOTA_FLAG();

int main()
{
    puts("yes\n");
    RC3_NOTA_FLAG();
    return 0;
}

void RC3_NOTA_FLAG()
{
    RC3_ROOT_1776 = 0x00031337;
    puts("This is not the flag you are looking for\n");
}
