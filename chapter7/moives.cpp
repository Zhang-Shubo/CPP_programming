#include <iostream>
#include <string>

using std::cout;using std::endl;

class movie
{
public:
  typedef std::string str;
  movie() = default;
  movie(str na,float r,str t):name(na),rate(r),ontime(t){};
  friend void clear(movie &m);

  inline str getName(){
    return name;
  }
  float getRate()
  {
    return rate;
  }

  movie &modifyName(str na)
  {
    name = na;
    return *this;
  }

private:
  str name = "";
  float rate = 0;
  str ontime = "";

};
void clear(movie &m)
{
  m.name = "None";
  m.rate = 0.0;
  m.ontime = "None";
}
int main()
{
  movie a,b("B",4.0,"2010");
  a.modifyName("A");
  //clear(a);
  cout << a.getName() << " " << b.getName() << endl;
  return 0;
}
