void a() {
  asm("mov r3, r0");
}

void b() {
  asm("mov r1, r0");
}

void c() {
  asm("mov r3, r0");
}

void handle() {
  char buf[100];

  gets(buf);
}

int main(int argc, char *argv[])
{
  setbuf(stdout, NULL);
  
  puts("montre moi tes pipes");

  handle();

  puts("po for");

  return 0;
}
