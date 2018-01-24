#include <iostream>
#include <string>

using std::cout;using std::endl;

//the distinction of class and struct is only
//private default and public default
class movie
{
public:
  typedef std::string str;
  //constructor
  movie() = default;
  movie(str na,float r,str t):name(na),rate(r),ontime(t){};
  //friend is not declearation
  friend void clear(movie &m);

  inline str getName(){
    return name;
  }
  float getRate()
  {
    return rate;
  }

//this is a pointer to object, generating automatically
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
//friend can use private menber
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
