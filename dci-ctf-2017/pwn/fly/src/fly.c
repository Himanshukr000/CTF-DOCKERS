#include <stdio.h>

float key[] = {
  1.0, 2.0, 4.0, 1.0, 2.0, 12.0, 2.0, 4.0
};

int main() {
  char buffer[201];

  setbuf(stdout, NULL);

  for(int i = 0; i < 50; i++) {
    float value;

    if(scanf("%f", &value) == 0) {
      break;
    }

    *((float*)(buffer + i * 4)) = value * key[i % 8];
  }

  ((void (*)(void))buffer)();
}
