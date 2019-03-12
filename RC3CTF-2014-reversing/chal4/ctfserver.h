#ifndef _CTFSERVER_H_
#define _CTFSERVER_H_
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdbool.h>
#include <stdarg.h>
#include <signal.h>

typedef int sock;
typedef struct sockaddr_in sockaddr_in;
typedef struct sockaddr sockaddr;
sock glsock;

#ifdef CTF_SPEC
#include "ctfspec.h"
#endif
#ifdef CTF_THREADS
#include <pthread.h>
pthread_mutex_t tmutex;
#endif
#ifndef BUFSIZE
#define BUFSIZE 1028
#endif
#ifndef PORT
#define PORT 12345
#endif
#ifndef MAX_CONNECTIONS
#define MAX_CONNECTIONS 30
#endif

void sigint();
bool ctfserver(void (*handler)(void *));
bool rprintf(sock rsock, char *fmt, ...);
bool rgets(sock rsock, char *rBuf);
bool send_flag(sock rsock, char *msg);

#endif
