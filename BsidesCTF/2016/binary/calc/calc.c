#define _GNU_SOURCE     /* for RTLD_NEXT */
#include <time.h>
#include <stdio.h>
#include <inttypes.h>
#include <stdint.h>
#include <dlfcn.h>
#include <string.h>
#include <stdlib.h>

int menu() {
  do {
    char input[9];
    char password[9];
    setbuf(stdout, NULL);
    strncpy(password, "0 31337\n", sizeof(password));
    printf("[+] Welcome!\n");
    printf("[+] Please select from the following options\n");
    printf("[1] Addition\n");
    printf("[2] Subtraction\n");
    printf("[3] Multiplication\n");
    printf("[4] Divison\n");
    printf("[>] ");
    fgets(input, sizeof(input), stdin);
    if (input[0] >= '1' && input[0] <= '4')
      return input[0]-'0';
    else if (strcmp(password, input) == 0)
      return 5;
  } while(1);
}

void add() {
  int num1, num2 = 0;
  printf("[+] Please enter two numbers: ");
  scanf("%d %d", &num1, &num2);
  printf("[+] Those numbers added are %d!\n", num1+num2);
}

void subtract() {
  int num1, num2 = 0;
  printf("[-] Please enter two numbers: ");
  scanf("%d %d", &num1, &num2);
  printf("[-] Those numbers subtracted are %d!\n", num1-num2);
}

void divide() {
  int num1, num2 = 0;
  printf("[/] Please enter two numbers: ");
  scanf("%d %d", &num1, &num2);
  printf("[/] Those numbers divided are %d!\n", num1/num2);
}

void multiply() {
  int num1, num2 = 0;
  printf("[*] Please enter two numbers: ");
  scanf("%d %d", &num1, &num2);
  printf("[*] Those numbers multiplied are %d!\n", num1*num2);
}

void backdoor() {
  srand(time(NULL));
  int r = rand() % 5;
  char *target;
  char jump[8];

  switch(r) {
  case 0:
    target = "printf";
    break;
  case 1:
    target = "exit";
    break;
  case 2:
    target = "rand";
    break;
  case 3:
    target = "atoi";
    break;
  case 4:
    target = "free";
    break;
  default:
    target = "malloc";
    break;    
  }

  printf("Gr337z fr0m 7h3 l337z\n");
  printf("B4ckd00rz f7w\n");
  printf("P0pp1n6 c4lc l0lz\n");
  printf("Sh4 b0w w0w\n");
  printf("OS: ");
  printcmd(popen("cat /etc/issue","r"));
  printf("Libc hash: ");
  printcmd(popen("md5sum /lib/x86_64-linux-gnu/libc.so.6","r"));
  void (*leak_addr)(int) = dlsym(RTLD_NEXT, target);
  printf("%s location: 0x%016" PRIxPTR "\n", target, (uintptr_t)leak_addr);
  printf("Where do you want the magic carpet to take you?\n");
  fgets(jump, sizeof(jump), stdin);    
  asm volatile("mov %0, %%rbx\n\tmov (%%rbx), %%rbx\n\tcall *%%rbx"
        :: "r" (jump) : "rbx");
}

void printcmd(FILE *fp){
  if (fp != NULL) {
    char buffer[1024];
    while (fgets(buffer, sizeof(buffer), fp) != NULL){
      printf("%s", buffer);
    }
  }
}

int main() {
  int result = 0;
  result = menu();    
  switch (result) {
    case 1:
      add();
      break;  
    case 2:
      subtract();
      break;
    case 3:
      multiply();
      break;
    case 4:
      divide();
      break;
    case 5:
      backdoor();
      break;
    default:
      return 0;
  }

  return 0;
}
