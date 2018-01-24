#include <iostream>
#include <string>

using namespace std;

char& getchar(string& s,string::size_type n = 1)
{
  if(n < s.size())
    return s[n];
  else
    return s[0];
}

int main()
{
  string str = "zhangshubo";
  getchar(str,0) = 'Z';

  cout << str << endl;
  return 0;
}
