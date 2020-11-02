#include <iostream>
#include <string>
#include <vector>
#include "sl_list.h"

using namespace std;

ListNode *addTwoNum(ListNode *l1,ListNode *l2){

  ListNode *preHead= new ListNode(0),*p=preHead;

  int extra = 0;
  l1 = l1->next;l2 = l2->next;
  while(l1||l2||extra){
    int sum = (l1? l1->val:0) + (l2? l2->val:0) + extra;
    p->next = new ListNode(sum%10);
    p = p->next;
    extra = sum/10;

    l1=l1 ? l1->next:l1;
    l2=l2 ? l2->next:l2;
  }
  return preHead;
}

int main()
{
  ListNode *l1 = creatList({1,2,3});
  ListNode *l2 = creatList({5,6,7});
  printList(l1);
  printList(l2);

  ListNode *sum = addTwoNum(l1, l2);
  printList(sum);

  destroyList(l1);
  destroyList(l2);
  destroyList(sum);
  return 0;
}
