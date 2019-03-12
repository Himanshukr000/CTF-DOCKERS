#include <stdio.h>

int main(int argc, char *argv[])
{
  char buf[256];

  FILE *f = fopen("/flag", "r");

  fread(buf, 256, 1, f);

  puts(buf);

  return 0;
}
