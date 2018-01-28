#include <iostream>
#include <string>

using namespace std;

int main()
{
    std::cout << "test" << std::endl;

    //test string braket
    string s = "123";
    int i = int(s[0]);

    cout << i << endl;

    //test nullptr

    int *p = NULL;

    cout << (p? 0:1) << endl;

    return 0;
}
