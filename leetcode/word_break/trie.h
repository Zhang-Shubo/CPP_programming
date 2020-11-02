#ifndef __TRIE_H__
#define __TRIE_H__

#include <vector>
#include <map>
#include <string>

/*trie node*/
struct node
{
    std::string* end = nullptr;
    std::map<char, node*> children = {};
};

/*trie have private member root*/
class trie
{

public:
    trie(){
        root = new node();
    }
    ~trie(){
        delete root;
    }
    // 如果root是一个静态指针怎么办？会调用析构函数中的删除动态指针吗？
    trie(node* root):root(root) {};
    void insert(const std::vector<std::string> vec);
    void insert(const std::string str);

    std::vector<int> prefixes(const std::string str);
    
    

private:
    node* root = nullptr;

};

#endif