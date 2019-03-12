#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

const char version[] = "v0.1.3";

int main(int argc, char *argv[])
{
  alarm(1);

  char *path = getenv("QUERY_STRING");

  chdir("public");

  FILE *f;

  if(path == 0 || strlen(path) == 0 || path[0] == '/') {
    f = fopen("index.html", "r");
  } else {
    char *amp = strchr(path, '&');
    if(amp != 0) *amp = 0;

    amp = strchr(path, '=');
    if(amp != 0) *amp = 0;

    f = fopen(path, "r");
  }

  puts("Content-Type: text/html\n");

  printf("<!");
  printf("--#set var=\"version\" value=\"%s\" -->", version);

  if(f) {
    int c;

    while(1) {
      c = fgetc(f);

      if(c == EOF) {
        break;
      } else {
        putchar(c);
      }
    }
  } else {
    puts("Error");
    return 1;
  }

  fflush(stdout);

  return 0;
}
