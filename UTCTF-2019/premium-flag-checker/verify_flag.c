#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <emscripten.h>

int verify_flag(char* candidate) {
    EM_ASM_({
            console.log($0);
    }, 43452);

    int a = EM_ASM_INT({
        return window.a;
    }); // 0x57d389b3

    int b = EM_ASM_INT({
        return window.b;
    }); 

    int c = EM_ASM_INT({
        return window.c;
    }); 

    int length = strlen(candidate);

    if(length * 2 + length * length != 1443) {
        return 0;
    }

    char* prefix = "utflag{";
    for(int i = 0; i < 7; i++){
        if(prefix[i] != candidate[i]){
            return 0;
        }
    }

    int encrypted[29] = {99, 113, 110, 103, 114, 127, 116, 115, 95, 107, 114, 95, 97, 65, 106, 115, 95, 112, 105, 110, 106, 127, 95, 100, 56, 45, 52, 106, 100};

    int key = a ^ b ^ c;
    for(int i = 7; i < length-1; i++){
        if(encrypted[i-7] != ((candidate[i] ^ (key << ((i % 4) * 8))) & 0xff)){
            return 0;
        }
    }

    if(candidate[length - 1] != '}'){
        return 0;
    }

    return 1;
}