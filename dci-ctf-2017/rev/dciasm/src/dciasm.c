#include <stdio.h>
#include <stdlib.h>

// unsigned char stack[256];
// unsigned char *sp = stack;
char program[1024] = {0};
char *base_addr = program;
unsigned short ip = 0;

unsigned short r1, r2, r3, r4;
unsigned short *registers[] = {&r1, &r2, &r3, &r4};

/*
void push(unsigned char value) {
  *sp = value;
  sp++;
}

unsigned char pop() {
  sp--;
  return *sp;
}
*/

void syscall() {
  switch(r1) {
  case 0:
    r1 = getchar();
    break;

  case 1:
    putchar(r2);
    break;

  case 2:
    exit(r2);
    break;

  default:
    puts("*** bad syscall ***");
    exit(-1);
    break;
  }

}

void set() {
  unsigned char reg = program[ip] & 3;

  ip += 1;
  *registers[reg] = *((unsigned short *)(program + ip));
  ip += 1;
}

void mov() {
  unsigned char r1 = program[ip] & 3;
  unsigned char r2 = (program[ip] >> 2) & 3;

  *registers[r1] = *registers[r2];
}

void add_reg() {
  unsigned char r1 = program[ip] & 3;
  unsigned char r2 = (program[ip] >> 2) & 3;

  *registers[r1] += *registers[r2];
}


void add() {
  unsigned char reg = program[ip] & 3;

  ip += 1;

  *registers[reg] += *((unsigned short *)(program + ip));

  ip += 1;
}

void mult() {
  unsigned char reg = program[ip] & 3;

  ip += 1;
  *registers[reg] *= *((unsigned short *)(program + ip));
  ip += 1;
}


void neg() {
  unsigned char reg = program[ip] & 3;
  *registers[reg] = ~*registers[reg];
}

void jump() {
  unsigned char reg = program[ip] & 3;
  ip = *registers[reg] - 1;
}

void jump_eq() {
  if(r1) {
    ip = r2 - 1;
  }
}


int main(int argc, char *argv[]) {
  puts("-- dciasm emulator --");
  if(argc != 2) {
    printf("usage: %s [input file]\n", argv[0]);
    exit(1);
  }

  FILE *fp = fopen(argv[1], "r");

  fread(program, 1, 1023, fp);

  while(1) {
    unsigned char inst = program[ip];

    // printf("r1 = %d, r2 = %d, ip = %d\n", r1, r2, ip);

    if(inst == 0xff) {
      syscall();
    } else if(inst >> 4 == 1) {
      set();
    } else if(inst >> 4 == 2) {
      mov();
    } else if(inst >> 4 == 3) {
      add();
    } else if(inst >> 4 == 4) {
      neg();
    } else if(inst >> 4 == 5) {
      mult();
    } else if(inst >> 4 == 6) {
      jump_eq();
    } else if(inst >> 4 == 7) {
      add_reg();
    }

    ip++;
  }

  return 0;
}
