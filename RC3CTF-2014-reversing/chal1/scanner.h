/* Name:      Jaime Geiger
 * Class:     CSCI-243 - Mechanics of Programming
 * Professor: TJ Borrelli
 * Project:   1 - Lexical Scanner
 * File:      scanner.h - Declarations of helper functions to the main
 *                        tokenize program. Also includes defines and typedefs
 */

#ifndef _SCANNER_H_
#define _SCANNER_H_
#include <stdlib.h> //needs to be included for FILE typedef

//defines
#define true 1
#define false 0
#define america(a) free(a) //:)
#define ERR_STATE 99
#define NUM_CC 12
#define BUFSIZE 256

//typedefs
typedef int bool;
typedef struct Node{ //one spot in the tm
    int tostate; //next state
    char storechr; //'d' or 's' as read in from the tm file
    bool store; //for ease, false if 'd', true if 's'
} Node;

//prototypes
Node ** get_matrix(FILE *fp, int states, int accept);
void print_matrix(Node **tm, int states);
void free_matrix(Node **tm, int states);
int get_char_class(char ch);
bool scanner(Node **tm, int start, int accept, char *sBuf);
int stoi(char* str);

#endif
