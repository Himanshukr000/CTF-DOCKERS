#include<iostream>
#include<sys/ptrace.h>
#include<string.h>
using namespace std;

//flag = FLAG{AnTI_D3buGGIng_I$_Fun}

//characters: AntI_D3buGng$F

void printbad()
{

	cout<<"\n\nYou are not supposed to debugg me....";
}

int lencheck(char input[20])
{
	int a = strlen(input) + 10;
	return a;
}

void printflag(char *p1, int length)
{
	int i = 0;
	cout<<"\n\nsea{";
	cout<< *(p1 + 0) << *(p1 + 1) << *(p1 + 2) << *(p1 + 3) << *(p1 + 4) << *(p1 + 5) << *(p1 + 6) << *(p1 + 7) << *(p1 + 8) << *(p1 + 9);
	cout<< *(p1 + 9) << *(p1 + 3) << *(p1 + 10) << *(p1 + 11) << *(p1 + 4) << *(p1 + 3) << *(p1 + 12) <<*(p1 + 4 ) << *(p1 + 13) << *(p1 + 8) << *(p1 + 10);
	cout<<"}sides";

}

int inpcheck(char *p1, int length, int debug)
{

	int  result1 = 0, result2 = 0,  i = length - 11, j = 0;
	char arr1[7], arr2[7];
	cout<<"\nPtrace1: "<<debug;
	if(((debug + 1) * 10) == 10)
	{

		if(length != 24)
		{	
			return 0;
		}
		
		else
		{

			while(i > (length - 18) && j < 7)
			{
				arr2[j] = *(p1 + i);
			
				i = i - 1;
				j = j + 1;		
			}

			if(strncmp(arr2,"buGng$F", 7))
			{
				result1 = 7;	

				if(result1 + 10 == 17)			
				{	
					i = 0;
			
					while(i <= j)
                			{
                        			arr1[i] = *(p1 + i);
                        			i = i + 1;
                			}

					if(strncmp(arr2,"AntI_D3",7))
                			{
                        			result2 = 7;
						printflag(p1, length);
						return result1 + result2;
                			}
			
					else
					{
						return 0;
					}
		
				}
				else
				{
					return 0;
				}
	
			}
			else
			{
				return 0;
			}
		
		}
	}
	else
	{
		printbad();
		return 0;	
	}
}


int main()
{
	
	int length, debug, result;
	char input[20], *p1;
	
	debug = ptrace(PTRACE_TRACEME, 0, 1, 0);

	cout<<"Enter Input:\n";
	cin>>input;
	
	length = lencheck(input);
	p1 = &input[0];
	
	result = inpcheck(p1, length, debug);
	if(result != 14)
	{
		cout<<"\n\nBetter Luck next time\n";
	}
	return 0;
}
