//gcc race.c -lpthread -o raceme
#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>

int maxval = 10000;
unsigned long globalval=0;

void initialize(){
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);
}

int subnumber(){
  int n;
  printf(">- ");
  scanf("%d",&n);
  getchar();
  if (1<=n && n<=250){
    maxval-=n;
    return 1;
  }
  else return 0;
}

int addnumber(){
  int n;
  printf(">+ ");
  scanf("%d",&n);
  getchar();
  
  int maxupdate=10000-maxval;
  if (1<=n && n<=250){
    if (n > maxupdate){
      n=maxupdate;
    } 
    maxval+=n; 
    return 1;
  }
  else return 0;
}

void* check(){
  while(maxval<=10000){
    if (maxval < 5000){
    for(unsigned long i=0;i<4294967295/2;i++);
    maxval+=4900;
    }
  } 
}

void* operations(){
  while(maxval>0){
    printf("1. ++ 0-250\n");
    printf("2. -- 0-250\n");
    printf(">> ");
    int ch;
    scanf("%d",&ch);
    getchar();
    switch (ch){
    case 1:
      addnumber();
      printf("Val is now %d\n",maxval);
      for(unsigned long i=0;i<4294967295/8;i++);
      break;
    case 2:
      subnumber();
      printf("Val is now %d\n",maxval);
      for(unsigned long i=0;i<4294967295/8;i++);
      break;
    default:
      exit(0);
    }
  }
}

void dostuff(){
  pthread_t thread_operations, thread_check;  
  pthread_create(&thread_operations, NULL, operations, NULL); 
  pthread_create(&thread_check, NULL, check, NULL); 
  pthread_join(thread_operations, NULL);
  if (maxval<0){
    system("/bin/sh");
    return;
    }
  else return;
}

int main(){
  initialize();
  dostuff();
  return 0;
}

    
