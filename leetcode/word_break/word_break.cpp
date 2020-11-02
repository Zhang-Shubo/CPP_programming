#include <iostream>
#include <deque>
#include <unordered_map>

#include "trie.h"


void recrusive(trie* t, std::string str, std::vector<int>& dp, int base){
    auto index = t->prefixes(str);
    if(index.empty()) return;
    for(auto &i:index){
        if(dp[base+i] != 0) continue;
        else
        {
            dp[base+i] = 1;
            recrusive(t, str.substr(i+1, str.size()), dp, base+i+1);
        }
        
    }
}

//检测字符串是否有符合规则的分割
bool detect(trie* t, std::string str){
    std::vector<int> dp(str.size(), 0);
    recrusive(t, str, dp, 0);
    return dp.back()== 1? true: false;
}



std::vector<std::string> word_break(std::string str, std::vector<std::string> vec){
    // 构建trie树
    trie* t = new trie();
    t->insert(vec);

    std::vector<std::vector<int>> res;
    auto length = str.size();
    //使用while替换递归，构建一个队列
    std::deque<int> not_end_q;
    not_end_q.push_back(0);

    std::unordered_map<std::string, std::vector<int>> mem;
    while (! not_end_q.empty())
    {
        int i = not_end_q.front();
        not_end_q.pop_front();

        //超过长度，继续下一个循环
        if(i>=length) continue;

        auto child_str = str.substr(i, length);
        if(!detect(t, child_str)) continue;
        std::vector<int> index;
        if(mem.find(child_str)!=mem.end()){
            continue;
        } 
        else{
            index = t->prefixes(child_str);
            mem[child_str] = index;
        }
        
        //没有搜索到前缀，继续下一个循环
        if(index.empty()) continue;

        //按顺序插入，方便剪枝
        for(auto &j:index){
            if(i+j+1==length) continue;
            if(not_end_q.empty()){
                not_end_q.push_back(i+j+1);
            }
            else
            {
                auto len = not_end_q.size();
                bool inserted = false;
                for(int k=0; k<len; k++){
                    if(not_end_q[k] <= i+j+1) continue;
                    else{
                        not_end_q.insert(not_end_q.begin()+k, i+j+1);
                        inserted = true;
                        break;
                    }
                }
                if(!inserted){
                    not_end_q.push_back(i+j+1);
                }
            }
            
            
        }

        if(i==0){
            for(auto &j:index){
                res.push_back(std::vector<int>({j+1}));
            }
        }
        else{
            std::vector<std::vector<int>> temp;
            for(auto &line:res){
                if(line.back()==i){
                    for(auto ind: index){
                        std::vector<int> ll(line);
                        ll.push_back(ind+i+1);
                        temp.push_back(ll);
                    }
                }
                else if(line.back()>i)
                {
                    temp.push_back(line);
                }
            }
            res = temp;
        }
    }
    //删除结尾不为最后的字符串
    std::vector<std::string> temp;
    for(auto &line:res){
        if(line.back()==length){
            std::string s = "";
            int start = 0;
            for(auto part:line){
                s+=str.substr(start,part-start);
                start = part;
                s+="_";
            }
            temp.push_back(s.substr(0,s.size()-1));
        }
    }
    return temp;
}



int main(){
    
    
    std::vector<std::string> v = {"aaaa","aaa", "aa", "a"};
    std::string ss = "aaaaaaaaaaaaaaaaa";
    auto res = word_break(ss, v);
    // for(auto r: res){
    //     std::cout << r << std::endl;
    // }
    return 0;
}
 