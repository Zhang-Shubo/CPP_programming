#include <iostream>

using namespace std;

int main()
{
  int *i = new int(100);

  int *j = NULL;
  //int *j = nullptr;
  int *k = i;

  *k = 6;
  cout << *i << endl;

  //delete i;
  cout << *k << endl;
  delete k;

  // delete null pointer is ok
  delete j;

  return 0;
}
