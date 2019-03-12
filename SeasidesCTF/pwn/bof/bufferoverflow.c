#include<stdio.h>

void initialize(){
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);
}

void den()
{
	int a,b;
	printf("Al Capone is impressed. You are almost done.\n");
	printf("Guess a number:\n");
	scanf("%d",&a);
	printf("Guess another number:\n");
	scanf("%d",&b);
	if(a+b<0 && a>0 && b>0)
	{
		system("cat flag.txt");
	}
	else
	{
		printf("Numbers failed to impress me.\n");
	}
}
int main()
{
	initialize();
	
	printf("You can get much farther with a kind word and a gun than you can with a kind word alone:\n");
	
	char buffer[64];
	
	gets(buffer);
	
	printf("I am like any other man. All I do is supply a demand.\n");
	
	return 0;
}
//gcc bufferoverflow.c -o classico -fno-stack-protector -m32 -no-pie -fno-pic -mpreferred-stack-boundary=3
