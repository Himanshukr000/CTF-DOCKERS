#include <stdio.h>
#include <stdlib.h>

int fail(){
    printf("Nope sorry :(\n");
    exit(-1);
}

int main(int argc, char *argv[]){
    char *buffer = NULL;
    char pass[32];
    char aoeu[] = "eys";
    int read, i, tmp;
    unsigned int len;
    tmp = 6;
    read = getline(&buffer, &len, stdin);
    if(-1 != read){
        strncpy(pass, buffer, 32);
    }else{
        printf("Failure...\n");
    }
    free(buffer);
    printf("%s\n", pass);
    for(i = 0; i < 5; i++){
        if(pass[tmp] != '_'){
            fail();
        }
        tmp+=6-i;
    }

    if(pass[0] != '\x4d'){
        fail();
    }

    if((pass[7] - pass[0]) != 0x14){
        fail();
    }

    if(pass[3] != '\x65'){
        fail();
    }

    if(pass[2] != '\x6b'){
        fail();
    }


    for(i = 0; i < 3; i++){
        if(pass[3+i] != aoeu[i]){
            fail();
        }
    }

    if(pass[11] == pass[13] && pass[13] == pass[16] && pass[16] == pass[5]+1){
    }else{
        fail();
    }
    if((pass[8] - 8) != (8*13)+2){
        fail();
    }

    if(pass[9] != 'e'){
        fail();
    }

    if(pass[10] - (pass[7] - pass[0]) != 0x5A){
        fail();
    }

    if(!(pass[14] - (14*7)+6)){
        fail();
    }

    if(!(pass[15] == pass[7])){
        fail();
    }

    if(pass[18] == 'b' && pass[19] == '\x61' && pass[20] == '\x64'){
        
    }else{fail();}


   if(pass[22] == ':' && pass[23] == ')'){
   }else{fail();}

   if(pass[25] != '!'){fail();}

    return 0;
}
