#include <stdio.h>
//#include <windows.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
char *flag_encoded = "8<#))=7(R:VEO57$P36$Q;6Y*17EP:CT]";
// add new flag'''
//sea{lolwtf}sides
//base64 tested
int base64(char* str){
  char table[65] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
  unsigned int len = strlen(str);

  char *new_buf = malloc(4 * (len / 3) + 1);
  memset(new_buf,0, 4*(len/3)+1);

  char *p = new_buf;
  int i;

  for ( i = 0; i < len - len % 3; i += 3 ) {
    unsigned int q = (str[i] << 16) + (str[i + 1] << 8) + str[i + 2];
    p[0] = table[(q >> 18) & 0x3F];
    p[1] = table[(q >> 12) & 0x3F];
    p[2] = table[(q >> 6)  & 0x3F];
    p[3] = table[str[i + 2] & 0x3F];
    p += 4;
  }
  if ( len % 3 == 1 ) {
    p[0] = table[((unsigned int)(str[i] << 16) >> 18) & 0x3F];
    p[1] = table[16 * str[i] & 0x3F];
    p[2] = '=';
    p[3] = '=';
    p += 4;
  }
  else if ( len % 3 == 2 ) {
    unsigned int q = (str[i] << 16) + (str[i + 1] << 8);
    p[0] = table[(q >> 18) & 0x3F];
    p[1] = table[(q >> 12) & 0x3F];
    p[2] = table[(q >> 6) & 0x3F];
    p[3] = '=';
    p += 4;
  }
  *p = 0;
  return new_buf;
}

int rot13(const char *str) {
  char *s = (char *)str;
  char *new_str = malloc(strlen(str) + 1);
  char *p = new_str;
  while ( *s ) {
    if ( *s <= '@' || *s > 'Z' ) {
      if ( *s <= '`' || *s > 'z' )
        *p = *s;
      else
        *p = (*s - 'T') % 26 + 'a';
    }
    else {
      *p = (*s - '4') % 26 + 'A';
    }
    ++p;
    ++s;
  }
  *p = 0;
  return new_str;
}

int uuencode(char *str) {
  char *new_str = malloc(4 * strlen(str) / 3 + 1);
  unsigned int len = strlen(str);
  memset(new_str,0, 4*(len/3)+1);
  char *s = str;
  char *p = new_str;
  unsigned int i;
  for ( i = strlen(str); i > 45; i -= 45 )
  {
  	p[0] = 'M';
    p++;
    for ( int j = 0; j <= 44; j += 3 )
    {
      if ( s[0] >> 2 )
        p[0] = (s[0] >> 2) + 32;
      else
        p[0] = 32;
      if ( 16 * s[0] & 0x30 )
        p[1] = (16 * s[0] & 0x30) + 32 | (s[1] >> 4);
      else
        p[1] = 32 | (s[1] >> 4);
      if ( 4 * s[1] & 0x3C )
        p[2] = ((4 * s[1] & 0x3C) + 32) | (s[2] >> 6);
      else
        p[2] = 32 | (s[2] >> 6);
      if ( s[2] & 0x3F )
        p[3] = (s[2] & 0x3F) + 32;
      else
        p[3] = 32;
      s += 3;
      p += 4;
    }
  }
  if ( i )
    *p = (i & 0x3F) + 32;
  else
    *p = 32;
  p++;
  for (int j = 0; j < i; j += 3 )
  {
    if ( s[0] >> 2 )
      p[0] = (s[0] >> 2) + 32;
    else
      p[0] = 32;
    if ( 16 * s[0] & 0x30 )
      p[1] = ((16 * s[0] & 0x30) + 32) | (s[1] >> 4);
    else
      p[1] = 32 | (s[1] >> 4);
    if ( 4 * s[1] & 0x3C )
      p[2] = ((4 * s[1] & 0x3C) + 32) | (s[2] >> 6);
    else
      p[2] = 32 | (s[2] >> 6);
    if ( s[2] & 0x3F )
      p[3] = (s[2] & 0x3F) + 32;
    else
      p[3] = 32;
    s += 3;
    p += 4;
  }
  *p = 0;
  return new_str;
}



int main(int argc, char **argv) {
  if ( argc != 2 ) {
    puts("please_find_me.exe <<key_goes_here>> ");
    exit(0);
  }
  char *input = (char *)malloc(strlen(argv[1]) + 1); //safekeeping :)
  memset(input,0,strlen(argv[1]) + 1);
  strncpy(input, argv[1], strlen(argv[1])); // oof safekeeping 2 :)
  char *flag = uuencode(rot13(base64(input)));
    if ( !strcmp(flag, flag_encoded) )
    puts("GG!, now put that flag on ye head and fly away!!");
  else
    puts("Nope, wrong flag ye got there m8, try again!");
  return 0;
}
