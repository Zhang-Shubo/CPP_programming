#ifndef __SL_LIST__
#define __SL_LIST__

#include <iostream>
#include <vector>

//the defination of single link list
struct ListNode{
  int val;
  ListNode *next;
  ListNode();
  ListNode(int i);
};

ListNode* creatList(const std::vector<int> &vec);
void printList(ListNode *preHead);
void clearList(ListNode *preHead);
void destroyList(ListNode *preHead);

#endif
