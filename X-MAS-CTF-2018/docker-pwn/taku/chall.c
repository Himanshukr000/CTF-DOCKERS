#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <ctype.h>
#include <sys/random.h>

typedef unsigned long long int volatile ullint;
typedef long long int volatile llint;

// get random offset -n +n
llint get_random_offset(llint n) {
    unsigned int seed;
    getrandom(&seed, sizeof(seed), GRND_RANDOM);
    srand(seed);
    return rand() % (2 * n + 1 - 0) - n;
}

FILE *f;
void read_flag(char *flag) {
    f = fopen("flag", "r");
    fscanf(f, "%s", flag);
    fclose(f);
}

int check_string1(char *buffer) {
    int n = strlen(buffer);


    char formats[] = {'d', 'i', 'o', 'u', 'x', 'X', 'e', 'E', 'f', 'F', 'g', 'G', 'a', 'A', 'c', 's', 'C', 'S', 'p', 'm', 'n'};

    int formlen = strlen(formats);



    int format = 0;

    for(int i = 0; i < n; i++) {
            if(buffer[i] == '%') {
                    if(!format) {
                        format = 1;
                    } else {
                        format = 0;
                    }
            } else {
                for(int j = 0; j < formlen; j++) {
                        if(buffer[i] == formats[j]) {
                                if(format) {
                                        if(buffer[i] != 'n') {
                                                return 0;
                                        }
                                        format = 0;
                                }
                        }
                }
            }

    }

    if(format) {
            return 0;
    }
    return 1;
}

int check_string2(char *buffer) {
    int n = strlen(buffer);

    for (int i = 0; i < n; i++) {
        if (buffer[i] == '%') {
            if (i == n-1)
                return 0;

            i++;
            while (buffer[i] >= '0' && buffer[i] <= '9' && i < n)
                i++;

            while (buffer[i] == 'h' && i < n - 1)
                i++;

            if (buffer[i] != 'n' && buffer[i] != '$')
                return 0;

            if (buffer[i] == '$') {
                if (i == n - 1)
                    return 0;
                else {
                    i++;
                    while (buffer[i] == 'h' && i < n - 1)
                        i++;

                    if (buffer[i] != 'n')
                        return 0;
                }
            }
        }
    }
    return 1;
}

void execute_op(char operation, ullint *dest, ullint arg1, ullint arg2) {
    switch (operation) {
                case '+':
                    *dest = arg1 + arg2;
                    break;
                case '-':
                    *dest = arg1 - arg2;
                    break;
                case '<':
                    *dest = arg1 < arg2;
                    break;
                case '>':
                    *dest = arg1 > arg2;
                    break;
                case '=':
                    *dest = arg1 == arg2;
                    break;
                default:
                    break;
            }
}

#define MAX_LEN 32
#define MAX_NUMS 128
#define MAX_OPS (MAX_NUMS / 2)
ullint register1;
ullint register2;
ullint calculate(char *buf, 
               ullint *numbers,
               ullint *result) {
    char tmp[MAX_LEN];
    //char restricted[MAX_NUMS];
   // memset(restricted, 0, MAX_NUMS);

    char operation = -1;
    char last_char;
    ullint tmp_idx = 0;
    ullint num_idx = 0;
    ullint len = strlen(buf);

    ullint in_num = 0;
    for (ullint i = 0; i < len; i++) {
        if (isdigit(buf[i]) && in_num) {
            tmp[tmp_idx++] = buf[i];
            last_char = buf[i];
        } else if (isdigit(buf[i]) && !in_num) {
            in_num = 1;
            tmp[tmp_idx++] = buf[i];
            last_char = buf[i];
        } else if (!isdigit(buf[i]) && in_num) {
            in_num = 0;
            tmp[tmp_idx] = 0;
            tmp_idx = 0;
            numbers[num_idx++] = atoi(tmp);
            last_char = buf[i];

            if (operation != -1) {
    		//if ((operation == '+' || operation == '-') && (restricted[num_idx - 1] || restricted[num_idx - 2])) { return 1; }
		    execute_op(operation,
                       &numbers[num_idx - 1],
                       numbers[num_idx - 2],
                       numbers[num_idx - 1]);
                operation = -1;
            }
        }

        if (!isdigit(buf[i])) {
            if (buf[i] == '+' ||
                buf[i] == '-' ||
                buf[i] == '>' ||
                buf[i] == '<' ||
                buf[i] == '=') {
                
                last_char = buf[i];
                operation = buf[i];
            } else if (buf[i] != ' '){
                int load = 0;
                switch (buf[i]) {
                    case '!': // load reg1
                        numbers[num_idx++] = register1;
                        load = 1;
                        break;
                    case '@': // load reg2
			//restricted[num_idx] = 1;
                        numbers[num_idx++] = register2;
                        load = 1;
                        break;
                    case '#': // save reg1
                        register1 = numbers[num_idx - 1];
                        break;
                    case '$': // save reg2
                        register2 = numbers[num_idx - 1];
                        break;
                    default:
                        break;
            
                }
                //printf("Registers %lx %lx\n", register1, register2);
                last_char = buf[i];
                if (load && operation != -1) {
		    //if ((operation == '+' || operation == '-') && (restricted[num_idx - 1] || restricted[num_idx - 2])) { return 1; }
                      execute_op(operation,
                       &numbers[num_idx - 1],
                       numbers[num_idx - 2],
                       numbers[num_idx - 1]);
                      operation = -1;
                }

            }
        }
    }
   
    tmp[tmp_idx] = 0;
    if (isdigit(last_char)) {numbers[num_idx++] = atoi(tmp);


	    //if ((operation == '+' || operation == '-') && (restricted[num_idx - 1] || restricted[num_idx - 2])) { return 1; }
    execute_op(operation,
                &numbers[num_idx - 1],
                numbers[num_idx - 2],
                numbers[num_idx - 1]);
    }

    //for (ullint i = 0; i < num_idx; i++) {
        //printf("%lx ", numbers[i]);
    //}
    //puts("");

    *result = numbers[num_idx - 1];
    return 0;
}

ullint main() {
    alarm(60);
    setbuf(stdin, 0); setbuf(stdout, 0); setbuf(stderr, 0);

    //llint rnd = get_random_offset(500000);
    //printf("%d\n", rnd);
    printf("SANTA CALCULATOR\n");
    
    char flag[MAX_LEN * 2];
    char buffer[MAX_LEN];
    buffer[MAX_LEN - 1] = 0; 

    read_flag(flag);
    
    // ---------------------------------------------
    //printf("%p %p ", flag, buffer);
    //printf("%s\n", flag);
    // ---------------------------------------------
  
    register2 = (size_t) buffer;
    ullint result = 0;
    ullint numbers[MAX_NUMS];
    ullint some_address = (size_t)buffer + get_random_offset(500000);
    //printf("%p\n", some_address);
    char *ptr = NULL;

    for (ullint tries = 0; tries < 45; tries++) {
        read(0, buffer, 31);
        if ((ptr = strchr(buffer, '\n')) != NULL) {
            *ptr = 0;
        }

        if (!check_string1(buffer) || !check_string2(buffer)) {
            printf("No, no, no\n");
            continue;
        }
    
        if (calculate(buffer, numbers, &result)) {
            printf("Oops\n");
            continue;
        }
       
        printf("CALCULATING ");
        printf(buffer);

        if (result == 1 || result == 0) {
            printf(" RESULT %d\n", result);
        } else {
            //printf("\n%p %p\n", some_address, register2);
            printf("\nSanta hates those big numbers...\n");
        }
        //printf("Registers %p %p %p\n", register1, register2, result);
    }

    return 0;
}
