//gcc patch.c -o patch
//4513 4513 14,4566 4569 576f726c,4574 4574 64,4540 4540 00,4452 4452 00,4628 4628 5d,8197 8203 2f62696e2f7368

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int normFunc(int x){
    if (x==0)return 1;
    else return x;
}

void nullfunc(){
    for(;;);
}
void nul1func(){
    system("apropos");
}

int main(){
    int a=5,b=4,c=21;
    if (a*b!=c)exit(1);
    if (normFunc(1))exit(1);
    
    char str1[]="Hello";
    char str2[]="World";
    if (strcmp(str1,str2))exit(1);
    nullfunc();

    return 0;
}
