#ifndef FUNCTIONS_H_INCLUDED
#define FUNCTIONS_H_INCLUDED

#include <fstream>
#include <iostream>
#include <algorithm>
#include <string>
#include <stdlib.h>
#include <time.h>
#include <string.h>

using std::ofstream;
using std::cout;
using std::string;
using std::to_string;

void gen_random(char *s, const int len);
void xor_string(char* txt, char* key, int txtlen);
void create_xored_data(char* txt, char* key, ofstream& output);

#endif // FUNCTIONS_H_INCLUDED