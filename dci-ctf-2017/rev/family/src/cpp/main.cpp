#include "../hpp/Jeremy.hpp"
#include "../hpp/Myriam.hpp"
#include "../hpp/Parker.hpp"
#include "../hpp/Yolonda.hpp"
#include "../hpp/Clement.hpp"
#include "../hpp/Oscar.hpp"
#include "../hpp/walk.hpp"

void walk_to_address(void* address)
{
    void (*go_to_address)();
    go_to_address = (void (*)())(address);

    cout << "Walking towards destination..." << std::endl;
    for (int i = 0; i < 45; i++) {
        walk(((unsigned char*)address)[i%4], 42*i);
        if (i == 44)
            go_to_address();
    }
}

int main()
{
    Oswaldo* jeremy = new Jeremy();
    Oswaldo* parker = new Parker();
    Oswaldo* clement = new Clement();
    Oswaldo* oscar = new Oscar();
    Oswaldo* yolonda = new Yolonda();
    Oswaldo* myriam = new Myriam();

    oscar->address6();

    cout << "Hint 1: This is a challenge about C++ inheritance. Think about what each" << std::endl;
    cout << "classes could represents in a family tree. For instance, a class inheriting" << std::endl;
    cout << "from Oscar would be considered his daughter or son." << std::endl << std::endl;

    cout << "Hint 2: Once you find Oscar's second cousin once removed, you will need to" << std::endl;
    cout << "call the correct method. The method you are looking for is the same method" << std::endl;
    cout << "that was called when Oscar first talked to you at the begining, but overidden" << std::endl;
    cout << "by the person you are looking for instead of Oscar." << std::endl << std::endl;

    cout << "Hint 3: Some family members object were already instanciated at the begining." << std::endl;
    cout << "It could be a good idea to start from there." << std::endl;

    cout << "Good luck! At what address do you want to go?" << std::endl;
    cout << "Address: ";

    void* address = 0;
    scanf("%p", &address);
    walk_to_address(address);

    return 1;
}