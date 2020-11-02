#include "sl_list.h"
using namespace std;
ListNode::ListNode() = default;
ListNode::ListNode(int i):val(i),next(NULL){};

//creatList from vector
ListNode* creatList(const std::vector<int> &vec){
  //setup the pre header
  ListNode *preHead = new ListNode(0);
  cout << "new a space" << endl;
  auto l = vec.size();
  for (decltype(l) i = 0;i < l; ++i)
  {
    ListNode *p = new ListNode(vec[i]);
    cout << "new a space" << endl;
    p->next = preHead->next;
    preHead->next = p;
  }
  return preHead;
}

//ouput the content of the list
void printList(ListNode *preHead)
{
  while (preHead->next){
    auto tmp = preHead->next;
    cout << tmp->val << endl;
    preHead = tmp;
  }
}

//clear the list reserve preHead
void clearList(ListNode *preHead)
{
  if ((preHead->next) != NULL){
    clearList(preHead->next);
  }
  delete preHead->next;
  cout << "free a space" << endl;
}

//free the list
void destroyList(ListNode *preHead)
{
  clearList(preHead);
  delete preHead;
  cout << "free a space" << endl;
}
