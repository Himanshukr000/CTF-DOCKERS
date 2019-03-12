#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>

#define MAX_PASSWORDS       6
#define MAX_PASSWORD_LEN    512
#define MAX_NAME_LEN        32

#define ADD_PASSWORD    1
#define CHANGE_PASSWORD 2
#define DELETE_PASSWORD 3
#define SHOW_PASSWORDS  4
#define EXIT_PROG       5

typedef struct
{
    ssize_t password_len;
    char    name[MAX_NAME_LEN];
    char*   value;
} Password;
Password passwords[MAX_PASSWORDS];

int recvdata(char* buf, int count)
{
    int c;
    int nb_read = 0;
    while ((c = getchar()) != '\n' && c != EOF) {
        if (nb_read < count) {
            buf[nb_read++] = c;
        }
    }
    return nb_read;
}

void clear_stdin()
{
    char c;
    while ((c = getchar()) != '\n' && c != EOF) {}
}

void init_passwords()
{
    int index = 0;
    for (index = 0; index < MAX_PASSWORDS; index++) {
        memset(&passwords[index], 0, sizeof(Password));
    }
}

int find_free_slot()
{
    int index = 0;
    for (index = 0; index <= MAX_PASSWORDS; index++) {
        if (index == MAX_PASSWORDS) {
            return -1;
        } else if (passwords[index].value == NULL) {
            return index;
        }
    }
}
void add_password()
{
    char password[MAX_PASSWORD_LEN];
    ssize_t bytesRead = 0;
    int index = find_free_slot();

    if (index == -1) {
        printf("\nYou can store at most %d passwords.\n", MAX_PASSWORDS);
        return;
    }

    printf("\nEnter your password's ID (i.e: what it's used for).\n> ");
    bytesRead = recvdata(passwords[index].name, MAX_NAME_LEN-1);
    passwords[index].name[bytesRead] = 0;

    printf("\nEnter your password.\n> ");
    bytesRead = recvdata(password, MAX_PASSWORD_LEN);

    passwords[index].password_len = bytesRead;
    passwords[index].value        = malloc(bytesRead);
    memcpy(passwords[index].value, password, bytesRead);
    passwords[index].value[bytesRead] = 0;

    printf("\nAdded password at index %d.\n", index);
}

void change_password()
{
    char password[MAX_PASSWORD_LEN];
    ssize_t bytesRead = 0;
    unsigned int choice;

    printf("\nEnter the password index you want to modify.\n> ");
    scanf("%u", &choice);
    clear_stdin();

    if (passwords[choice].value == NULL) {
        printf("\nThere are no passwords at index %d\n", choice);
        return;
    }

    printf("\nEnter your new password.\n> ");
    bytesRead = recvdata(password, MAX_PASSWORD_LEN);

    if (bytesRead > passwords[choice].password_len) {
        passwords[choice].value = realloc(passwords[choice].value, bytesRead);
    }

    passwords[choice].password_len = bytesRead;
    memcpy(passwords[choice].value, password, bytesRead);
    passwords[choice].value[bytesRead] = 0;

    printf("\nPassword at index %d has been modified.\n", choice);
}

void delete_password()
{
    unsigned int choice;
    printf("\nEnter the password index you want to delete.\n> ");
    scanf("%u", &choice);
    clear_stdin();

    if (choice >= MAX_PASSWORDS) {
        puts("Invalid choice!");
        return;
    }

    free(passwords[choice].value);
    passwords[choice].value = NULL;
    //memset(&passwords[choice], 0, sizeof(Password));
    printf("\nDeleted password at index %d.\n", choice); 
}

void show_passwords()
{
    unsigned int i = 0;
    unsigned int j = 0;

    printf("\nPasswords (hex):");
    for (i = 0; i < MAX_PASSWORDS; i++) {
        if (passwords[i].value == NULL) {
            printf("\n%d - Free", i);
        } else {
            printf("\n%s: [", passwords[i].name);
            for (j = 0; j < passwords[i].password_len; j++) {
                printf("%02x", passwords[i].value[j] & 0xff);
            }
            printf("]");
        }
    }
    printf("\n ");
}

void menu()
{   
    unsigned int choice = 0;

    while (choice != EXIT_PROG) {
        printf("\nChoose an option:\n"
             "1 - Add password\n"
             "2 - Change password\n"
             "3 - Delete password\n"
             "4 - Show passwords\n"
             "5 - Exit\n> ");
        scanf("%u", &choice);
        clear_stdin();

        switch (choice)
        {
            case ADD_PASSWORD:      add_password();     break;
            case CHANGE_PASSWORD:   change_password();  break;
            case DELETE_PASSWORD:   delete_password();  break;
            case SHOW_PASSWORDS:    show_passwords();   break;
            case EXIT_PROG:         exit(0);
            default:
                puts("Invalid choice!");
        }
    }
}

int main()
{
    // ==================== everything here will be erased ====================
    int permission = PROT_READ|PROT_EXEC|PROT_WRITE;
    
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    init_passwords();

    puts("\nWelcome to SecurePasswords, the best password manager ev3r!");
    system("date");
    mprotect((void*)0x401000, 2278, permission);
    memset(main, 0x00, (long)&&f_end - (long)main);
    // ========================================================================
f_end:  
    permission = PROT_READ|PROT_EXEC;
    mprotect((void*)0x401000, 2278, permission);
    printf("-----------------------------------------------------------\n ");
    menu();
}