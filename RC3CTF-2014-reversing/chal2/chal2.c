#ifndef CTF_THREADS
#define CTF_THREADS
#endif
#include "ctfserver.h"
#include <signal.h>

void handler(void * pSock);

sock gsock;

int main()
{
    if (!ctfserver(handler)) return 1;
    return 0;
}

void sig_handler(){
    pthread_mutex_unlock(&tmutex);
    send_flag(gsock, "You've won Charlie!\n");
    close(gsock);
    pthread_exit(NULL);
}

void seg_handler(){
    pthread_exit(NULL);
}

void handler(void *pSock){
    sock rsock = *((sock *)pSock);
    int int1, int2;
    char sBuf[BUFSIZE];
    char rBuf[BUFSIZE];
    memset(rBuf, '\0', BUFSIZE);
    memset(sBuf, '\0', BUFSIZE);
    signal(SIGFPE, sig_handler);
    signal(SIGPIPE, SIG_IGN);
    signal(SIGSEGV, seg_handler);

    if (!rprintf(rsock, "Enter a number: ")) goto Cleanup;

    if (!rgets(rsock, rBuf)) goto Cleanup;
    int1 = atoi(rBuf);

    if (!rprintf(rsock, "Enter another number: ")) goto Cleanup;
    int1 = atoi(rBuf);

    if (!rgets(rsock, rBuf)) goto Cleanup;

    int2 = atoi(rBuf);

    pthread_mutex_lock(&tmutex);
    gsock = rsock;
    int ans = int1 / int2;
    pthread_mutex_unlock(&tmutex);
    if (!rprintf(rsock, "%d divided by %d equals: %d\n", int1, int2, ans)) goto Cleanup;

Cleanup:
    close(rsock);
    pthread_exit(NULL);
}
