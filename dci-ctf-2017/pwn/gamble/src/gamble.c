#include <stdio.h>
#include <stdlib.h>
#include <time.h>

unsigned int coins = 100;

void menu() {
  printf("You have %d coins.\n", coins);
  printf("1. Gamble (cost 1 coin)\n");
  printf("2. Set your name\n");
  printf("3. Quit\n");
}

void gamble() {
  if(coins > 0) {
    coins--;

    if(rand() % 10 == 0) {
      printf("You won!\n");
      coins += 1;
    } else {
      printf("You lost...\n");
    }
  } else {
    printf("You don't have enough coins. Bye.\n");
    exit(0);
  }
}

void set_name() {
  printf("What is your name?\n");

  char buffer[256] = {0};

  fgets(buffer, 255, stdin);

  printf("Hello ");
  printf(buffer);
  printf("Enjoy gambling!\n");
}

int main(int argc, char *argv[]) {
  int choice = 0;

  alarm(30);

  srand(time(0));
  setbuf(stdout, NULL);

  while(1) {
    menu();

    if(coins >= 500) {
      printf("Wooo how is that possible? Get out!\n");
      system("cat /home/gamble/flag");
      exit(0);
    }

    choice = getchar();
    int tmp;

    while ((tmp = getchar()) != '\n' && tmp != EOF);

    switch(choice) {
    case '1':
      gamble();
      break;

    case '2':
      set_name();
      break;

    case '3':
      return 0;

    default:
      printf("Invalid choice.\n");
      break;
    }

    if(feof(stdin)) break;
  }

  return 0;
}
