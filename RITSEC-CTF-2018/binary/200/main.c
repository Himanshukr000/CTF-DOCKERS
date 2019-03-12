#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <getopt.h>

int sanitize(char *in){
    unsigned int len = strlen(in);
    for(int i = 0; i < len; i++){
        if(in[i] == ';' || in[i] == '`' || in[i] == '\n' || in[i] == '$' || in[i] == '|' || in[i] == '(' || in[i] == ')' || in[i] == '&'){
            in[i] = ' ';
        }
    }
}


int main(int argc, char **argv){
    char buf[32];
    char *error = malloc(32);
    int c;
    char *cvalue = NULL;
    strncpy(error, "Error   \0", 9);

    while((c = getopt(argc,argv, "e:")) != -1){
        switch(c){
            case 'e':
                free(error);
                error = optarg;
                break;

        }
    }

    while(fgets(buf, 32, stdin)){
    }
    sanitize(buf);
    char command[64];
    sprintf(command, "echo %s || echo %s | figlet | lolcat  && echo %s | figlet | lolcat ", buf, error, buf);

    system(command);
}





