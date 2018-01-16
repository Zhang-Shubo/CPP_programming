#include <iostream>
#include <vector>

using namespace std;

int main()
{
  vector<int> nums = {1,3,5,7};
  for (auto it = nums.begin();it != nums.end(); ++it)
    cout << *it << endl;
  return 0;
}
