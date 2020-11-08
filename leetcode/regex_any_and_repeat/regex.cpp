#include <iostream>

#include <string>


bool isMatch2(std::string s, std::string p) {
    if(p.empty()) return s.empty();
    
    auto first_match = (!s.empty() && (s[0] == p[0] || p[0] == '.'));
    
    if(p.length() >= 2 && p[1] == '*'){
        return isMatch2(s, p.substr(2)) || (first_match && isMatch2(s.substr(1), p));
    }
    else{
        return first_match && isMatch2(s.substr(1), p.substr(1));
    }
}

bool isMatch(const char* s, const char* p) {
    if(*p == 0) return *s == 0;
    
    auto first_match = *s && (*s == *p || *p == '.');
    
    if(*(p+1) == '*'){
        return isMatch(s, p+2) || (first_match && isMatch(++s, p));
    }
    else{
        return first_match && isMatch(++s, ++p);
    }
}

bool isMatch3(std::string s, std::string p) {
    return isMatch(s.c_str(), p.c_str());
}
    


int main(){
    std::string ss = "a*aabbccc";
    std::string pp = "aabbcc";
    std::cout << isMatch3(pp, ss) << std::endl;
    return 0;
}