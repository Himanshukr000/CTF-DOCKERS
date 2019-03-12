#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "pwnable_harness.h"

void assembled()
{
	char flag[100];
	FILE* solved = fopen("flag.txt", "r");
	while (fgets(flag, sizeof(flag), solved))
	{
		printf("%s", flag);
	}
}

void end_of_journey()
{
	char end[500];
	char zero[500];
	printf("Please take the unique string (line above the C code) from each of the four paths, combine them in this order (North, East, West, South) in one line and submit it.\n");
	fgets(end, sizeof(end), stdin);
	FILE* assembled_pieces;
	assembled_pieces = fopen("0", "r");
	fgets(zero, sizeof(zero), assembled_pieces);
	if (strncmp(zero, end, 5) == 0)
	{
		printf("Congratz, you've survived the wasteland.\n");
		assembled();
	}
	
}

void pathfinding(FILE* piece)
{
	
	char line[999];
	while (fgets(line, sizeof(line), piece))
	{
		printf("%s", line);
	}
/*
        FILE* piece;
        piece = fopen("test.txt", "r");
        pathfinding(piece);
*/
}

long djb2hash()
{
	char input[11];
	fgets(input, 10, stdin);
	size_t nl = strlen(input) - 1;
	input[nl] = '\0';
	unsigned char *str = input;
	unsigned long hash = 5381;
	int c;
	while (c = *str++)
	{
		hash = ((hash << 5) + hash) + c;
	}	
	long int deliverable = hash;
	return hash;	
}

static void handle_connection(int sock)
{
	FILE* piece;

	puts("North, South, East, or West? Or have you reached the End?");
	
	char input[500];

	fgets(input, 50, stdin);


	if (strncmp(input, "End", 3) == 0)
	{
		printf("So you think you've found the end?\n");
		end_of_journey();
	}

	if (strncmp(input, "North", 5) == 0)
	{
		printf("You head North, towards the mammoth mountains.\n");
		char string[20];
		char answer[20];
		char given[20];
		fgets(string, sizeof(string), stdin);
		strcpy(given, "wasteland");
		printf("%s\n", given);
		fgets(answer, sizeof(answer), stdin);
		strcat(string, given);
		int str_len = strlen(string);
		int user_size = atoi(answer);
		if (str_len == user_size)
		{
			char final_prompt[20];
			int final_int;
			char final_answer[20];
			fgets(final_prompt, sizeof(final_prompt), stdin);
			final_int = atoi(final_prompt);
			final_int = final_int >> 2;
			final_int = final_int << 4;
			final_int = final_int >> 1;
			final_int = final_int << 4;
			final_int = final_int >> 4;
			final_int = final_int << 9;
			final_int = final_int >> 5;
			final_int = final_int << 4;
			final_int = final_int >> 3;
			final_int = final_int << 2;
			fgets(final_answer, sizeof(final_answer), stdin);
			int last_piece = atoi(final_answer);
			if (final_int == last_piece)
			{
				piece = fopen("1", "r");
				pathfinding(piece);
			}
			
		}	
	}

	if (strncmp(input, "East", 4) == 0)
	{
		printf("You head East, to the Great Warlands.\n");
		char xbuf0[20];
		char xbuf1[20];
		char xbuf2[20];
		char xbuf4[20];
		fgets(xbuf0, sizeof(xbuf0), stdin);
		fgets(xbuf1, sizeof(xbuf1), stdin);
		fgets(xbuf2, sizeof(xbuf2), stdin);
		int xint0 = atoi(xbuf2);
		int xint1 = 0xdead;
		int product;
		product = xint0 ^ xint1;
		if (product == 50)
		{
			int final_x;
			int xint2 = 0x0;
			int xint3 = 0xffffffff;
			int xint4;
			xint3 = xint1 | xint0;
			xint0 = xint2 | xint0;
			xint4 = xint3 | xint1;
			xint2 = xint4 | xint0;
			xint1 = xint3 | xint2;
			xint0 = xint3 & xint2;
			xint1 = xint0 & xint4;
			xint2 = xint1 ^ xint3;
			xint3 = xint0 ^ xint2;
			xint4 = xint4 ^ xint2; 
			fgets(xbuf4, sizeof(xbuf4), stdin);
			final_x = atoi(xbuf4);
			if (xint4 == final_x)
			{
				piece = fopen("2", "r");
				pathfinding(piece);
			}
		}
	}

	if (strncmp(input, "West", 4) == 0)
	{
		printf("You head West, towards the green sea.\n");
		int i = 1;
		while (i<50)
		{
			i = i*2;
			printf("The more you wander, the more you find.\n");
		}

		char buf0[100];
		int check = 0;
		fgets(buf0, sizeof(buf0), stdin);
		check = atoi(buf0);
		if (check == i)
		{
			int i2 = 2;
			int i3;
			for (i = 0; i < 20; i++)
			{
				i2 = i2 *2;
				i2 = i2 + 245;
				i2 = i2 * 1785;
				i3 = i2 % 2354;
			}
			char buf1[50];
			fgets(buf1, sizeof(buf1), stdin);
			i2 = atoi(buf1);
			if (i2 == i3)
			{
				piece = fopen("3", "r");
				pathfinding(piece);
			} 
		}
	
	}
	if (strncmp(input, "South", 5) == 0)
	{
		printf("You head South, to the endless marshes.\n");
		float f;
		char buf0[5];
		fgets(buf0, sizeof(buf0), stdin);
		f = atof(buf0);

		if (f < 12.684125)
		{
			puts("Too much");
			exit(0);
		}

		if (f > 12.684125)
		{
			puts("Too little");
			exit(0);
		}
		
		else
		{
			int hi;
			printf("Please enter 5 characters to get hashed (btw this is really an x86 binary)\n");
			long hash = djb2hash();
			char hash_prompt[10];
			
			fgets(hash_prompt, sizeof(hash_prompt), stdin);
			unsigned long hash_user = atol(hash_prompt);
			if (hash == hash_user)
			{
				printf("They match\n");
				piece = fopen("4", "r");
				pathfinding(piece);
			}
			
		}
		
	}
}

int main(int argc, char** argv) {
	server_options defaults = {
		.user = "wasteland",
		.chrooted = true,
		.port = 10002,
		.time_limit_seconds = 30
	};
	
	return server_main(argc, argv, defaults, &handle_connection);
}
