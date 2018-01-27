#include <iostream>
#include <algorithm>
#include <list>

using namespace std;
int main()
{
  list<int> li = {1,2,3,4};

  // add element at first and last
  li.push_front(0);
  li.push_back(5);

  // the first element and the last element
  cout << li.front() << " " << li.back() <<  endl;

  //if find the value ,if not find return the end of range
  auto vali = find(li.cbegin(),li.cend(),2);
  cout << "The value is :" << (vali == li.cend() ? "none." : "found!") << endl;

  return 0;
}
