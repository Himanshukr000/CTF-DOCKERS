# Binary 250

## Analysis

- The binary provides functionalities to create, edit, delete and print the content of a struct. This is the typical characteristic of heap-based exploitation.
- The binary is written is golang and C. There are C functions being called in the golang code. This makes reverse engineering the binary slightly harder but the binary is not stripped, so we can navigate the functions pretty easily.
- The binary is vulnerable to Use-After-Free because the print function doesn't check if a pointer is freed or not.
- The binary is vulnerable to heap buffer-overflow because the edit function allows arbitrary input length.
- The struct is as following

```C
struct Person {
    void (*myFunc)(struct Person *);
    char *name;
    unsigned int age;
}
```

## Exploitation

### Bypassing ASLR

- This version of glibc is vulnerable to memory disclosure. It allows leaking `main_arena` address and therefore one can calculate the base address of libc
- This is done by allocating 2 chunks not in the fast bin range (> 0x80), then free the first chunk. The address of `main_arena` will be written in the fd and bk pointer of this free chunk. Then by leveraging UAF, we can print out this address

### Execute code

- By leveraging the heap buffer-overflow, we can overwrite the function pointer in each struct with `system` and trigger the function call by using the print functionality