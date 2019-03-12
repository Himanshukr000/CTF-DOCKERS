#include "ctfserver.h"

void handler(void * pSock);

int main()
{
    if (!ctfserver(handler)) return 1;
    return 0;
}

void handler(void * pSock){
    sock rsock = *((sock*)pSock);
    char sBuf[BUFSIZE];
    char rBuf[BUFSIZE];
    memset(rBuf, '\0', BUFSIZE);
    memset(sBuf, '\0', BUFSIZE);
    if (!rprintf(rsock, "The binaries can be found by going to http://rc3ctf.havefuninside.us/\n")) goto Cleanup;
    if (!rprintf(rsock, "What is a stack but a collection of things ready to be smashed ;)\nGive it to me: ")) goto Cleanup;
    if (!rgets(rsock, rBuf)) goto Cleanup;
    if (!rprintf(rsock, "\n")) goto Cleanup;
    volatile unsigned int q = 0;
    volatile unsigned int i = 0;
    char buf[512];
    strcpy(buf, rBuf);

    if (i == 0xDDAAAADD){
        if (!rprintf(rsock, "Almost")) goto Cleanup;
        for (int i = 0; i < 5; ++i){
            sleep(1);
            if (!rprintf(rsock, ".")) goto Cleanup;
        }
        if (!rprintf(rsock, "\n")) goto Cleanup;

        if (q == 0xDDEEEEDD){
            send_flag(rsock, "You win! Here is your flag: ");
            goto Cleanup;
        } else
            if (!rprintf(rsock, "No. i = %p; q = %p\n", i, q)) goto Cleanup;
    }else
        if (!rprintf(rsock, "No. i = 0x%x; q = 0x%x\n", i, q)) goto Cleanup;

Cleanup:
    close(rsock);
    return;
}
