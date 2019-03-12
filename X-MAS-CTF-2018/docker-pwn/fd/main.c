#include <stdlib.h>
#include <stdio.h>
#include <string.h>

FILE *fp;
char name[512];
long off;
long size;
//long end;
char *ptr;
long read_size;
char choice[10];

void win() {
system("cat flag");
}

int main() {
    alarm(60);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    //setvbuf(stderr, NULL, _IONBF, 0);
    close(2);
    char buffer[512];
    memset(buffer, 0, 512);

    puts("Welcome to the Santa's Archive");
    printf("Name a document to open: ");

    fgets(name, 511, stdin);
    ptr = strchr(name, '\n');
    if (ptr!= NULL){
        *ptr = 0;
    }

    if (strstr(name, "flag") != NULL) {
        printf("This is a secret document!\n");
        exit(0);
    }

    if (strstr(name, "stdin") != NULL) {
	printf("Ughh, so naughty. There are other ways to do this too.\n");
	exit(0);
    }


	printf("Do you want to read from other offset than 0? (y/n) \n");
   	fgets(choice, 5, stdin);
    printf("How much should we read: ");
    scanf("%d", &size);

    fp = fopen(name, "r");
    if (fp == NULL) {
        puts("Can't open the file");
        exit(0);
    }
    /*end = ftell(fp);
    rwind(fp);

    if (off > end) {
        puts("Your are trying to read outside of the document");
        exit(0);
   }
*/
  
 
    if (strstr(choice, "y") != NULL) {

    printf("Read register from offset: ");
    scanf("%d", &off);
    	fseek(fp, off, SEEK_SET);
    }
    read_size = fread(buffer, size, 1, fp);
    fclose(fp);

    printf("Content: ");
    fwrite(buffer, size, 1, stdout);

    return 0;
}
