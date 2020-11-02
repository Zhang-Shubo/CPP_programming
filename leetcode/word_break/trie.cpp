#include "trie.h"


void trie::insert(const std::string str){
    //这里面this可以省略，什么时候不能省略
    auto head = this->root;
    for(auto i=str.cbegin(); i<str.cend(); i++){
        // 这里是否会用内存泄漏？
        head->children.insert({*i, new node()});
        head = head->children[*i];
    }
    // 这里是否会有内存泄漏
    head->end = new std::string(str);
}

// 插入一个列表
void trie::insert(const std::vector<std::string> vec) {
    for(auto i=vec.cbegin(); i<vec.cend(); i++){
        this->insert(*i);
    }
}

std::vector<int> trie::prefixes(std::string str){
    std::vector<int> res;
    auto head = this->root;
    auto length = str.size();
    for(int i=0;i<length;i++){
        auto exist_node = head->children.find(str[i]);
        if(exist_node == head->children.end()) break;
        else{
            if(exist_node->second->end){
                res.push_back(i);
            }      
        }
        head = exist_node->second;
    }
    return res;

}