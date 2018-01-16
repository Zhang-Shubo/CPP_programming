#include <iostream>
#include <vector>
#include "chapter6.h"

using namespace std;
//vector<int> findSum(vector<int> nums,int sum);

vector<int> findSum(vector<int> nums,int sum)
{
  int i=0,j=0;
  vector<int> re;
  for (auto it_i = nums.begin();it_i != nums.end();++it_i){
    j = i + 1 ;
    for (auto it_j = (it_i+1);it_j != nums.end();++it_j){
      if (*it_i + *it_j == sum){
        re.push_back(i);
        re.push_back(j);
        return re;
      }
      j++;
    }
    i++;
  }
}

int main()
{
  vector<int> nums{1,3,6,9,7};
  int sum = 10;

  vector<int> re = findSum(nums,sum);

  auto it = re.begin();
  while(it != re.end())
    cout << *it++ << endl;

  return 0;
}
