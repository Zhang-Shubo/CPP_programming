#include <iostream>
#include <string>

using namespace std;

string::size_type findChar(const string &str, char c , string::size_type &occur)
{
  auto re = str.size();
  for(decltype(re) i = 0; i != str.size(); ++i){
    if (str[i] == c){
      re = i;
      occur++;
    }
  }
  return re;
}

int main()
{
  string str = "zhangshubobo";
  string::size_type occur = 0;
  const string s1 = "zhangshubo";
  //string s2 = s1;

  auto last_position = findChar("strstrstr",'s',occur);

  cout << last_position << " " << occur << endl;
}
