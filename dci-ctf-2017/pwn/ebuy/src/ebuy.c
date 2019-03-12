#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>

#define MAX_ITEMS 8
#define NAME_SIZE 28
#define ITEM_TYPE_FOOD  0xA0
#define ITEM_TYPE_OTHER 0xB0
#define ITEM_TYPE_FLAG  0xC0
#define ITEM_TYPE_NONE  0xD0

typedef struct
{
    int type;
    char name[20];
    void* item_data;
} Item;

typedef struct
{
    int is_edible;
} Food;

typedef struct
{
    char value[32];
} Flag;

typedef struct
{
    char desc[32];
} Other;

Item* items;
char* flag;

void recvline(char* buf, size_t count)
{
    char tmp[count];
    char c;

    fgets(tmp, count, stdin);
    if (!strchr(tmp, '\n')) {
        while ((c = getchar()) != '\n' && c != EOF) {}
    }
    tmp[strcspn(tmp, "\n")] = 0;
    strcpy(buf, tmp);
}

void clear_stdin()
{
    char c;
    while ((c = getchar()) != '\n' && c != EOF) {}
}

int make_choice(int min, int max)
{
    unsigned int choice = -1;
    scanf("%u", &choice);
    clear_stdin();
    while(choice < min || choice > max)
    {
        printf("Incorrect choice.\n> ");
        scanf("%u", &choice);
        clear_stdin();
    }
    return choice;
}

int find_free_slot()
{
    int index = 0;
    for (index = 0; index <= MAX_ITEMS; index++) {
        if (index == MAX_ITEMS) {
            return -1;
        } else if (items[index].type == ITEM_TYPE_NONE) {
            return index;
        }
    }
}

void buy_item()
{
    unsigned int choice;
    char input[64];
    Item new_item;
    int index = 0;
    int i = 0;

    index = find_free_slot();
    if (index == -1) {
        printf("\nYou have too many items.\n");
        return;

    }

    printf("\nChoose item type:\n"
         "1 - Food\n"
         "2 - Flag\n"
         "3 - Other\n> ");
    choice = make_choice(1, 3);

    if (choice == 1) {

        new_item.type = ITEM_TYPE_FOOD;
        new_item.item_data = malloc(sizeof(Food));
        printf("\nWhat kind of food do you want to buy?\n> ");
        recvline(new_item.name, NAME_SIZE);
        ((Food*)new_item.item_data)->is_edible = 1;

    } else if (choice == 2) {

        new_item.type = ITEM_TYPE_FLAG;
        new_item.item_data = malloc(sizeof(Flag));
        strcpy(new_item.name, "FLAG");
        for (i = 0; i < 32; i++) {
            ((Flag*)new_item.item_data)->value[i] = flag[i];
        }
    } else if (choice == 3) {

        new_item.type = ITEM_TYPE_OTHER;
        new_item.item_data = malloc(sizeof(Other));
        printf("\nWhat is the name of your item?\n> ");
        recvline(new_item.name, NAME_SIZE);
        printf("\nWhat is the description of your item?\n> ");
        recvline(((Other*)new_item.item_data)->desc, NAME_SIZE);

    }

    items[index] = new_item;
    printf("\nAdded %s at index %d\n", items[index].name, index);
}

void sell_item()
{
    unsigned int choice;
    printf("\nWhat is the index of the item you want to sell?\n> ");
    choice = make_choice(0, MAX_ITEMS-1);
    if (items[choice].type != ITEM_TYPE_FLAG) {
        items[choice].type = ITEM_TYPE_NONE;
        free(items[choice].item_data);
        puts("Item has been freed.");
        items[choice].item_data = NULL;
    } else {
        printf("Flags are too precious to be sold!");
    }
}

void show_items()
{
    printf("\n--------------ITEMS-------------");
    int index = 0;
    for (index = 0; index < MAX_ITEMS; index++) {
        if (items[index].type == ITEM_TYPE_FOOD) {
            Food* food = (Food*)items[index].item_data;
            printf("\n%d) Food: %s\n", index, items[index].name);
        } else if (items[index].type == ITEM_TYPE_FLAG) {
            printf("\n%d) FLAG: (private value)\n", index);
        } else if (items[index].type == ITEM_TYPE_OTHER) {
            Other* other = (Other*)items[index].item_data;
            printf("\n%d) %s: %s\n", index, items[index].name, other->desc);
        } else {
            printf("\n%d) No item\n", index);
        }
    }
    printf("--------------------------------");
    printf("\n");
}

void setup_items()
{
    items = malloc(sizeof(Item)*MAX_ITEMS);
    int index = 0;
    for (index = 0; index < MAX_ITEMS; index++) {
        items[index].type = ITEM_TYPE_NONE;
        items[index].item_data = NULL;
    }
}

void setup_flag()
{
    FILE *file;
    flag = malloc(32);
    file = fopen("/home/ebuy/flag", "r");
    if (file) {
        fread(flag, 1, 32, file);
        fclose(file);
    } else {
        printf("\nfopen error: %d (%s)", errno, strerror(errno));
        exit(1);
    }
}


int main()
{
    unsigned int choice;

    setbuf(stdin, NULL);
    setbuf(stdout, NULL);

    setup_items();
    setup_flag();

    while(1) {
        printf("\nChoose an option:\n"
             "1 - Buy item\n"
             "2 - Sell item\n"
             "3 - Show items\n"
             "4 - Quit\n> ");
        choice = make_choice(1, 4);

        if (choice == 1) {
            buy_item();
        }

        if (choice == 2) {
            sell_item();
        }

        if (choice == 3) {
            show_items();
        }

        if (choice == 4) {
            exit(0);
        }

    }
}