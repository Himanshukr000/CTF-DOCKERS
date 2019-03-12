/* Name:      Jaime Geiger
 * Class:     CSCI-243 - Mechanics of Programming
 * Professor: TJ Borrelli
 * Project:   1 - Lexical Scanner
 * File:      tokenize.c - the main file, tokenizes input based on a
 *                         transition matrix
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "classes.h"
#include "scanner.h"


/* Function:    main
 * Description  Recognize tokens based on a transition matrix (tm)
 * Parameters:  int argc - The number of arguments passed via the command line
 *              char **argv - array of arguments passed via the command line
 * Return Val:  0 on success, 1 on error
 */
int main(int argc, char **argv){
    //check if one extra arg for the tm file, if more or less: exit gracefully
    if (argc != 2){
        fprintf(stderr, "usage: ./%s tmfile\n", argv[0]);
        return 1;
    }

    //open file and make sure the file descriptor is valid before continuing
    FILE *fp;
    if (!( fp = fopen(argv[1], "r") )){
        perror(argv[1]);
        return 1;
    }

    int states, start, accept = -1; //top three lines of the tm file
    char buf[BUFSIZE]; //file read buffer
    char *ptr; //Will be null when done reading

    //Get state information from the first 3 lines
    for (int i=0; i<3; ++i){
        if ( (ptr = fgets(buf, 256, fp)) != NULL){
            if (strstr(buf, "states") != NULL){
                strtok(buf, " ");
                states = stoi(strtok(NULL, " "));
            }
            if (strstr(buf, "start") != NULL){
                strtok(buf, " ");
                start = stoi(strtok(NULL, " "));
            }
            if (strstr(buf, "accept") != NULL){
                strtok(buf, " ");
                accept = stoi(strtok(NULL, " "));
            }
        }
    }

    //Quit if one or more of the state information lines was not found
    if ( start == -1 || states == -1 || accept == -1){
        fprintf(stderr, "Did not get all required information "
                "from file (states, start, accept)\n");
                return 1;
    }

    //Populate the matrix, if the ptr is null then exit*/
    Node **tm = get_matrix(fp, states, accept);
    if (tm == NULL){
        fprintf(stderr, "Something is wrong with the tm file.\n");
        return 1;
    }
    fclose(fp);

    //print the matrix
    print_matrix(tm, states);

    //Allocate a buffer to hold the stored chars and fill it with null chars
    char *sBuf = (char *)malloc(sizeof(char) * BUFSIZE);
    memset(sBuf, '\0', BUFSIZE);

    /* scan until EOF. If the buffer is empty then reject, if not then something
     * was recognized and it will be printed to the screen */
    while (scanner(tm, start, accept, sBuf)){
        if (!strcmp(sBuf, ""))
            printf("rejected\n");
        else
            printf("recognized '%s'\n", sBuf);
    }

    /* Print that the end of file has been reached, free tm and
     * the stored buffer */
    printf("EOF\n");
    america(sBuf);
    free_matrix(tm, states);

}
