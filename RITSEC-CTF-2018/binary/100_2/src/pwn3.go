package main

/*
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "pwn3.h"
*/
import "C"

import (
	"fmt"
	"os/exec"
	"io/ioutil"
)

var pwn = func () {
	exec.Command("/bin/sh")
}

func vuln() {
	fmt.Println("not pwned")
}

func main() {
	C.init()

	buffer := C.malloc(16)
	_ = C.malloc(100)
	data, err := ioutil.ReadFile("flag.txt")
	
	if err != nil {
		panic(err)
	}

	_ = C.CBytes(data)
	
	fmt.Println("Gimme some bytes, I'm hangry...")
	C.myGets((*C.char)(buffer))
	fmt.Printf("mmmmm...., your ")
	C.myPrint((*C.char)(buffer))
	fmt.Printf(" is so good. Thanks. Bye.")
}
