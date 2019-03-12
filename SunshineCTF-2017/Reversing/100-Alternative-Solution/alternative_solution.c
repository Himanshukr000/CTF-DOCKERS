#include <stdlib.h>
#include <stdio.h>
#include "pwnable_harness.h"

static void handle_connection(int sock) {
	char buf0[10];
	float var0;
	fgets(buf0, sizeof(buf0), stdin);
	var0 = atof(buf0);
	if (var0 < 37.35928559) {
		printf("Too low just like you're chances of reaching the bottom.\n");
		exit(0);
	}
	
	if (var0 > 37.35928559) {
		printf("Too high just like your hopes of reaching the bottom.\n");
		exit(0);
	}
	else {
		FILE* flag;
		char rflag[50];
		flag = fopen("flag.txt", "r");
		while (fgets(rflag, sizeof(rflag), flag)) {
			printf("%s", rflag);
		}
	}
}

int main(int argc, char** argv) {
	server_options defaults = {
		.user = "alt",
		.chrooted = true,
		.port = 10001,
		.time_limit_seconds = 30
	};
	
	return server_main(argc, argv, defaults, &handle_connection);
}
