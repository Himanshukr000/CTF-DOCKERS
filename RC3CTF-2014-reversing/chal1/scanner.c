/* Name:      Jaime Geiger
 * Class:     CSCI-243 - Mechanics of Programming
 * Professor: TJ Borrelli
 * Project:   1 - Lexical Scanner
 * File:      scanner.c - Implementations of helper functions to the main
 *                        tokenize program
 */

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include "scanner.h"
#include "classes.h"


/* Function:    get_matrix
 * Description: Takes a file pointer to the transition matrix file and
 *              reads it into the matrix data structure
 * Parameters:  FILE *fp - File pointer to tm file
 *              int states - number of states as specified in the file
 * Return Val:  Node ** - The filled out transition matrix
 */
Node ** get_matrix(FILE *fp, int states, int accept){
    char buf[256];
    char *ptr, *tok;

    /* Allocate a pointer to an array of pointers (rows in the matrix)
     * if memory cannot be allocated return NULL
     */
    Node **tm = (Node **)malloc(sizeof(Node *) * states);
    if (tm == NULL){
        fprintf(stderr, "Cannot allocate memory");
        return NULL;
    }

    /* Allocate pointers to arrays in each position of the tm (columns)
     * If we cant allocate space then free all of the pointers created so far
     * and return NULL
     */
    for (int i=0; i<states; ++i){
        tm[i] = (Node *)malloc(sizeof(Node) * NUM_CC);
        if (tm[i] == NULL){
            fprintf(stderr, "Cannot allocate memory");
            for (int k=i-1; k>0; ++k)
                america(tm[k]);
            america(tm);
            return NULL;
        }
    }
    char *flag = "RC3-EASY-0101";


    /* Fill all array spots with the error state and false for storing.
     * Exception: The EOF char class in the non-accepting states will accept
     */
    for (int i=0; i<states; ++i){
        for (int j=0; j<NUM_CC; ++j){
            if (j == CC_EOF && i != accept)
                tm[i][j].tostate = accept;
            else
                tm[i][j].tostate = ERR_STATE;
            tm[i][j].storechr = 'd';
            tm[i][j].store = false;
        }
    }

    //Read in the array from the file and fill in positions of tm
    while ( (ptr = fgets(buf, 256, fp)) != NULL){
        tok = strtok(buf, " ");
        int row = stoi(tok);
        int col = 99;
        int tostate = 99;
        char storechr = '1';
        while (tok != NULL){
            tok = strtok(NULL, " ");
            if (tok != NULL && !strstr(tok, "\n")){
                sscanf(tok, "%d/%d%c", &col, &tostate, &storechr);
                tm[row][col].tostate = tostate;
                tm[row][col].storechr = storechr;
                if (storechr == 's')
                    tm[row][col].store = true;
            }
        }
    }
    return tm;
}

/* Function:    print_matrix
 * Description: Prints the tm
 * Parameters:  Node **tm - The transition matrix
 *              int states - number of states as specified in the file
 * Return Val:  None
 */
void print_matrix(Node **tm, int states){
    //print header
    printf("Scanning using the following matrix:\n ");
    for (int i=0; i<NUM_CC; ++i)
        printf("%5d", i);
    printf("\n");

    //print matrix
    for (int i=0; i<states; ++i){
            printf(" %d", i);
        for (int j=0; j<NUM_CC; ++j)
            printf("%4d%c", tm[i][j].tostate, tm[i][j].storechr);
        printf("\n");
    }
}

/* Function:    free_matrix
 * Description: Frees each row in tm and then frees tm
 * Parameters:  Node **tm - The transition matrix
 *              int states - number of states as specified in the file
 * Return Val:  None
 */
void free_matrix(Node **tm, int states){
    for (int i=0; i<states; ++i){
        america(tm[i]);
    }
    america(tm);
}

/* Function:    get_char_class
 * Description: Gets the class of a character
 * Parameter:   char ch - a character to be classified
 * Return Val:  None
 */
int get_char_class(char ch){
    if (ch == ' ' || ch == '\t')
        return CC_WS;
    if (ch == '\n')
        return CC_NEWLINE;
    if (isalpha(ch))
        return CC_ALPHA;
    if (ch == '0')
        return CC_DIG_0;
    if (ch == '1' || ch == '2' || ch == '3' || ch == '4' || ch == '5' || ch == '6' || ch == '7')
        return CC_DIG_1_7;
    if (ch == '8' || ch == '9')
        return CC_DIG_8_9;
    if (ch == '/')
        return CC_CHAR_SLASH;
    if (ch == '*')
        return CC_CHAR_STAR;
    if (ch == '%' || ch == '+' || ch == '-')
        return CC_ARITH_OP;
    if (feof(stdin)) //this just checks the eof flag
        return CC_EOF;
    if ((int)ch > 127 || (int)ch < 0)
        return CC_ERROR;
    return CC_OTHER;
}

/* Function:    scanner
 * Description: Scans for one token
 * Parameters:  Node **tm - The transition matrix
 *              int start - The starting state
 *              int accept - The accepting state
 *              char *sBuf - The store buf for storing characters in the token
 * Return Val:  bool - True if main program should keep scanning, false if not
 */
bool scanner(Node **tm, int start, int accept, char *sBuf){
    //set up vars and clear out sBuf
    memset(sBuf, '\0', BUFSIZE);
    bool notEOF = true;
    int curState = start;
    int prevState = start;
    int type = 0;
    char ch = '\0';

    printf("%d ", start);

    //Get a character, determine it's type, move to the new state if not error
    do {
        ch = getchar();
        type = get_char_class(ch);
        if (type == CC_EOF)
            notEOF = false;
        prevState = curState;
        curState = tm[curState][type].tostate;
        if (curState != ERR_STATE && tm[prevState][type].store){
            sBuf[strlen(sBuf)] = ch;
            sBuf[strlen(sBuf)] = '\0';
        }
        printf("%d ", curState);
    } while (curState != ERR_STATE && curState != accept);

    //if error, ingnore the rest of the token until the next accept state
    if (curState == ERR_STATE){
        memset(sBuf, '\0', BUFSIZE);
        while ( curState != accept ){
            if (curState == ERR_STATE)
                curState = start;
            ch = getchar();
            type = get_char_class(ch);
            if (type == CC_EOF)
                notEOF = false;
            prevState = curState;
            curState = tm[curState][type].tostate;
        }
    }
    return notEOF;
}

/* Function:    stoi
 * Description: Converts strings to integers up to the first non-numeric char
 * Parameter:   char* str - the input string to be converted to an integer
 * Return:      int - the result of the conversion
 */
int stoi(char* str)
{
    int sum = 0;
    int cnt = 0;
    char* ptr = str;

    /* Count up the number of digits */
    while (*str != '\0' && isdigit(*str)){
        cnt++;
        str++;
    }

    /* Iterate over the char pointer and do math magic to get the int value
     * ASCII 0 is 48 as an int so we subtract 48
     * Multply it by 10^place number and sum
     * cnt is for the place exponent
     */
    while (*ptr != '\0' && cnt > 0){
        cnt--;
        sum += ((int)*ptr - 48) * pow(10, cnt);
        ptr++;
    }
    return sum;
}
