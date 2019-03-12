//gcc srop.c -fstack-protector -o srop -fpie

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void syscall_(){
  __asm__("syscall; ret;");
}

void set_rax(){
  __asm__("movl $0xf, %eax; ret;");
}

void initialize(){
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);
}

int strt0k(char thestr[], char badstr[]){
    for(int i=0;i<strlen(thestr);i++){
        if(thestr[i]==badstr[0]){
            if(thestr[i+1]==badstr[1])
            return 1;
        }
    }
    return 0;
}

void attack(){
  char name[100];
  char enemy[100];
  printf("And you are, Mr. ?? ");
  scanf("%s",name);
  getchar();
  char baddie1[]="%n";
  char baddie2[]="%hn";
  char baddie3[]="%hhn";
  char baddie4[]="$n";
  char baddie5[]="$hn";
  char baddie6[]="$hhn";
  if (strt0k(name, baddie1))exit(0);
  if (strt0k(name, baddie2))exit(0);
  if (strt0k(name, baddie3))exit(0);
  if (strt0k(name, baddie4))exit(0);
  if (strt0k(name, baddie5))exit(0);
  if (strt0k(name, baddie6))exit(0);
  printf("Enemy is in hiding Mr. ");
  printf(name);
  printf(", can you still drop a shell?\n");
  fgets(enemy,500,stdin);
  return;
}

int main(){
  initialize();
  attack();
  return 0;
}
