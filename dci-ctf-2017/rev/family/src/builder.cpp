// g++ family_builder.cpp -o builder -std=c++0x

#include <fstream>
#include <iostream>
#include <algorithm>
#include <string>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <map>

using std::ofstream;
using std::cout;
using std::string;
using std::to_string;
using std::map;

#define NB_OF_FUNCTIONS 50
#define KEY_SIZE        40

void gen_random(char *s, const int len)
{
    static const char alphanum[] =
        "0123456789"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz";

    for (int i = 0; i < len; ++i)
    {
        s[i] = alphanum[rand() % (sizeof(alphanum) - 1)];
    }

    s[len] = 0;
}

void xor_string(char* txt, char* key, int txtlen)
{
    int keylen = strlen(key);
    int i = 0, j = 0;

    for (i = 0; i < txtlen; ++i, j = (j+1)%keylen)
    {
        txt[i] = txt[i] ^ key[j];
    }
}

void create_xored_data(char* txt, char* key, ofstream& output)
{
    int txtlen = strlen(txt)+1;
    int i = 0;

    xor_string(txt, key, txtlen);

    output << "char msg[] = {";
    for (i = 0; i < txtlen; i++) {
        if (i != 0)
            output << ", ";
        output << to_string((int)txt[i]);
    }
    output << ", 0};" << std::endl;
}

map<int, const char*> people = {
    {1, "Oswaldo"}, {2, "Piper"}, {3, "Loren"}, {4, "Delora"}, {5, "Hugh"},
    {6, "Arletta"}, {7, "Sherwood"}, {8, "Elvie"}, {9, "Abraham"},
    {10, "Maybell"}, {11, "Rolf"}, {12, "Kathey"}, {13, "Wilburn"},
    {14, "Daisey"}, {15, "Levi"}, {16, "Addie"}, {17, "Antony"}, {18, "Nellie"},
    {19, "Raleigh"}, {20, "Waneta"}, {21, "Oscar"}, {22, "Lourie"},
    {23, "Rudolf"}, {24, "Sherrie"}, {25, "Ryan"}, {26, "Silvana"},
    {27, "Gavin"}, {28, "Roxana"}, {29, "Burl"}, {30, "Antonetta"},
    {31, "Gordon"}, {32, "Aleshia"}, {33, "Manuel"}, {34, "Darci"},
    {35, "Donnie"}, {36, "Kathryn"}, {37, "Faustino"}, {38, "Janett"},
    {39, "Cory"}, {40, "Hermina"}, {41, "Jeremy"}, {42, "Myriam"},
    {43, "Parker"}, {44, "Yolonda"}, {45, "Clement"},
};

int main(int argc, char** argv)
{
    /* initialize random seed: */
    srand (time(NULL));

    if (argc != 2 && argc != 4)
    {
        cout << "Usage: ./family_builder [user_id] or ./family_builder [user_id] [parent_id1] [parent_id2]" << std::endl;
        return 0;
    }
    string person  = string(people[atoi(argv[1])]);
    string father = argc == 4 ? string(people[atoi(argv[2])]) : "";
    string mother = argc == 4 ? string(people[atoi(argv[3])]) : "";

    // create family member cpp
    ofstream cpp((person + ".cpp").c_str());
    cpp << "#include \"../hpp/" + person + ".hpp\"" << std::endl << std::endl;
    for (int i = 0; i < NB_OF_FUNCTIONS; i++)
    {
        char key[KEY_SIZE];
        char msg[] = "You went to the wrong address...";
        gen_random(key, KEY_SIZE);

        cpp << "void " + person + "::address" + to_string(i) + "()" << std::endl;
        cpp << "{" << std::endl;
        cpp << "\tchar key[] = \"" + string(key) + "\";" << std::endl;
        cpp << "\t";
        create_xored_data(msg, key, cpp);
        cpp << "\txor_string(msg, key, sizeof(msg)-1);" << std::endl;
        cpp << "\tcout << string(msg) << std::endl << std::endl;" << std::endl;
        cpp << "}" << std::endl << std::endl;
    }

    // create family member hpp
    ofstream hpp((person + ".hpp").c_str());
    string header_guard = person + "_H_INCLUDED";
    std::transform(header_guard.begin(), header_guard.end(),header_guard.begin(), ::toupper);
    hpp << "#ifndef " + header_guard << std::endl;
    hpp << "#define " + header_guard << std::endl << std::endl;

    if (father == "")
    {
        hpp << "#include \"functions.hpp\"" << std::endl << std::endl;
        hpp << "class " + person << std::endl;
    }
    else
    {
        hpp << "#include \"" + mother + ".hpp\"" << std::endl;
        hpp << "#include \"" + father + ".hpp\"" << std::endl << std::endl;
        hpp << "class " + person + " : public " + father + ", public " + mother << std::endl;
    }

    hpp << "{" << std::endl;
    hpp << "public:" << std::endl;
    for (int i = 0; i < NB_OF_FUNCTIONS; i++)
    {
        hpp << "\tvirtual void address" + to_string(i) + "();" << std::endl;
    }
    hpp << "};" << std::endl << std::endl;

    hpp << "#endif // " + header_guard;

    return 0;
}