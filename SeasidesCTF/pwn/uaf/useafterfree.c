#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void initialize(){
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);
}

int main()
{
	initialize();
	char* a = malloc(70);
	char* b = malloc(256);
	char* c;
	char s[100];
	strcpy(a, "change me.");
	int x,y;
	int cnt=0;
	int sw;
	while(1)
	{
		int f=0;
		printf("1.Add\n");
		printf("2.Subtract\n");
		printf("3.Multiply\n");
		printf("4.Divide\n");
		printf("5.Feedback\n");
		printf("6.Exit\n");
		scanf("%d",&sw);
		switch(sw)
		{
			case 1:
				printf("Enter two integers\n");
				scanf("%d%d",&x,&y);
				printf("%d\n",x+y);
				if(cnt==5)
				{
					free(a);
				}
				break;
			case 2:
				printf("Enter two integers\n");
				scanf("%d%d",&x,&y);
				printf("%d\n",x-y);
				cnt++;
				break;
			case 3:
				printf("Enter two integers\n");
				scanf("%d%d",&x,&y);
				printf("%d\n",x*y);
				cnt--;
				break;
			case 4:
				printf("Enter two integers\n");
				scanf("%d%d",&x,&y);
				printf("%d\n",x/y);
				printf("%s\n",a);
				if(strcmp(a,"$h1k4r1")==0)
				{
					printf("Use After Free is fun.");
					system("cat ./flag.txt");
					return 0;
				}
				break;
			case 5:
				c=malloc(60);
				printf("Enter your feedback:\n");
				char s[100];
				scanf("%s",&s);
				strcpy(c,s);
				printf("Thank you for your feedback!\n");
				break;
			case 6:
				f=1;
				break;
			default:
				printf("Invalid Input!\n");		
		}
		if(f==1)
		{
			break;
		}
	}
	return 0;
}

//gcc useafterfree.c -o allocator -no-pie -m32
