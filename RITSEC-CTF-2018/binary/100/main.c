#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fptr;
    char key[16];
    int valid = 0;
    char c;

    printf("Please enter your API key\n");
    gets(key);

    if(valid == 1){
        fptr = fopen("flag.txt","r");
        c = fgetc(fptr);
        while( c != EOF ){
            printf("%c", c);
            c = fgetc(fptr);
        }
        fclose(fptr);
    }
    printf("%d\n ", valid);
}
