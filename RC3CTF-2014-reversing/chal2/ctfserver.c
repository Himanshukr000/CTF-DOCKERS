#include "ctfserver.h"

void sigint(){
    close(glsock);
    exit(1);
}

bool ctfserver(void (*handler)(void *)) {
    signal(SIGINT, sigint);
    sock rsock, lsock;
    sockaddr_in lsin, rsin;
    memset(&lsin, 0, sizeof(sockaddr_in));
    memset(&rsin, 0, sizeof(sockaddr_in));

    lsin.sin_family = AF_INET;
    lsin.sin_port = htons(PORT);
    lsin.sin_addr.s_addr = htonl(INADDR_ANY);

    if ((lsock = socket(AF_INET, SOCK_STREAM, 0)) == -1){
        perror("socket");
        return false;
    }
    if (bind(lsock, (sockaddr *)&lsin, sizeof(lsin)) == -1){
        perror("bind");
        return false;
    }
    if (listen(lsock, MAX_CONNECTIONS) == -1){
        perror("listen");
        return false;
    }

    socklen_t rsin_len = sizeof(rsin);
#ifdef CTF_THREADS
    pthread_t pid;
    if ( pthread_mutex_init(&tmutex, NULL) != 0 ){
        perror("mutex init failed");
        close(lsock);
        return false;
    }
#endif

    glsock = lsock;
    while (1){
        if ((rsock = accept(lsock, (sockaddr *)&rsin, &rsin_len)) != -1){
#ifdef CTF_THREADS
            pthread_mutex_lock(&tmutex);
            pthread_create(&pid, NULL, (void *)handler, (void *)&rsock);
            pthread_mutex_unlock(&tmutex);
#else
            pid_t pid = fork();
            if (!pid){
                handler((void *)&rsock);
                close(rsock);
                return true;
            }else
                close(rsock);
#endif
        }
    }
    close(lsock);
    return true;
}

bool rprintf(sock rsock, char *fmt, ...){
    char msg[BUFSIZE];
    memset(msg, 0, BUFSIZE);
    va_list args;
    va_start(args, fmt);
    vsnprintf(msg, BUFSIZE, fmt, args);
    va_end(args);
#ifdef CTF_THREADS
    pthread_mutex_lock(&tmutex);
#endif
    if (send(rsock, msg, strlen(msg), 0) == -1){
        perror("send");
#ifdef CTF_THREADS
    pthread_mutex_unlock(&tmutex);
#endif
        return false;
    }
#ifdef CTF_THREADS
    pthread_mutex_unlock(&tmutex);
#endif
    return true;
}

bool rgets(sock rsock, char *rBuf){
    memset(rBuf, 0, BUFSIZE);
    if (recv(rsock, rBuf, BUFSIZE, 0) == -1){
        perror("recv");
        return false;
    }
    return true;
}

bool send_flag(sock rsock, char *msg){
    char fBuf[BUFSIZE];
    FILE *fp = fopen("flag.txt", "r");
    if (!fp)
        return rprintf(rsock, "%s%s\n", msg, "No flag.txt");
    fgets(fBuf, BUFSIZE, fp);
    fclose(fp);
    return rprintf(rsock, "%s%s\n", msg, fBuf);
}
