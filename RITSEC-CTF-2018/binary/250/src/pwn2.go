package main
/*
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "pwn2.h"
*/
import "C"

import (
	"unsafe"
	"fmt"
)

func realCreatePerson() {
	fmt.Println("Creating a new person...")
	
	if (C.createPerson() == 1) {
		fmt.Println("Failed creating a person.")
		return
	}

	person := C.p[C.numPerson]
	
	var nameLen int
	fmt.Printf("Enter name length: ")
	fmt.Scanf("%d", &nameLen)

	namePointer := C.malloc((_Ctype_size_t)(nameLen))
	person.name = unsafe.Pointer(namePointer)
	fmt.Printf("Enter person's name: ")
	C.myGets(person.name, 0x1337)

	fmt.Printf("Enter person's age: ")
	fmt.Scanf("%d", &person.age)

	C.numPerson += 1
}

func realEditPerson() {
	fmt.Println("Editting a person...")

	var idx C.uint
	fmt.Printf("Enter person's index (0-based): ")
	fmt.Scanf("%d", &idx)
	if idx < 0 || idx >= C.maxPerson {
		fmt.Println("Invalid index.\n")
		return
	}

	person := C.p[idx]

	var nameLen C.uint
	fmt.Printf("Enter new name length: ")
	fmt.Scanf("%d", &nameLen)

	fmt.Printf("Enter the new name: ")
	C.myGets(person.name, nameLen)	

	fmt.Println("Done.")
}

func realPrintPerson() {
	fmt.Println("Printing a person...")
	var idx C.uint
	fmt.Printf("Enter person's index (0-based): ")
	fmt.Scanf("%d", &idx)
	if idx < 0 || idx >= C.maxPerson {
		fmt.Println("Invalid index.\n")
		return
	}

	C.printPersonWrapper(idx)
}

func realDeletePerson() {
	fmt.Println("Delete a person...")

	var idx C.uint
	fmt.Printf("Enter person's index (0-based): ")
	fmt.Scanf("%d", &idx)
	if idx < 0 || idx >= C.maxPerson {
		fmt.Println("Invalid index.\n")
		return
	}

	C.deletePerson(idx)
	fmt.Println("Done.")
}

func printMenu() {
	fmt.Println("Welcome to yet another human resources management framework!")
	fmt.Println("============================================================")
	fmt.Println("1. Create a new person")
	fmt.Println("2. Edit a person")
	fmt.Println("3. Print information about a person")
	fmt.Println("4. Delete a person")
	fmt.Println("5. This framework sucks, get me out of here!")
	fmt.Printf("Enter your choice: ")
}

func main() {
	C.init()

	for {
		printMenu()
		var choice int
		fmt.Scanf("%d", &choice)
		fmt.Println("")

		switch choice {
		case 1:
			realCreatePerson()
		case 2:
			realEditPerson()
		case 3:
			realPrintPerson()
		case 4:
			realDeletePerson()
		case 5:
			return
		default:
			fmt.Println("Invalid choice.\n")
		}
		fmt.Println("")
	}
}