#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

typedef struct Person {
    void (*myFunc)(struct Person *);
    void *name;
    unsigned int age;
} Person;

#define MAX_NUM_PERSON 10

const unsigned int maxPerson = MAX_NUM_PERSON;
unsigned int numPerson = 0;
Person *p[MAX_NUM_PERSON];

static void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
}

static void myGets(void *s, unsigned int len) {
    read(0, (char *) s, len);
}

static void myPrint(void *s) {
    printf("%s\n", (char *) s);
}

static void printPerson(Person *person) {
    printf("Name: %s\n", (char *) (person -> name));
    printf("Age: %u\n", person -> age);
}

static unsigned int createPerson() {
    if (numPerson >= MAX_NUM_PERSON) {
        printf("No more person for you.\n");
        return 1;
    }

    Person *newP = (Person *) malloc(sizeof(Person));
    newP -> myFunc = printPerson;
    p[numPerson] = newP;
    return 0;
}

static unsigned int printPersonWrapper(unsigned int idx) {
    Person *P = p[idx];
    (P -> myFunc)(P);
}

static void deletePerson(unsigned int idx) {
    Person *P = p[idx];
    free(P -> name);
    free(P);
}