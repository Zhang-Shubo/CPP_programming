# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insert(li):
    head = p = None
    for i in li:
        if not head:
            head = p = ListNode(val=i)
            continue
        node = ListNode(i)
        p.next = node
        p = p.next
    return head


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        dummy = ListNode(-1)
        r = dummy
        mod = 0
        up = 0
        while p1 and p2:
            mod = (p1.val + p2.val + up)%10
            up = (p1.val + p2.val + up)//10

            r.next = ListNode(val=mod)
            r = r.next
            p1 = p1.next
            p2 = p2.next
        while p1:
            p1.val = (p1.val + up)%10
            up = (p1.val + up)//10
            r.next = p1
            r = r.next
            p1 = p1.next
        
        while p2:
            p2.val = (p2.val + up)%10
            up = (p2.val + up)//10
            r.next = p2
            r = r.next
            p2 = p2.next
        return dummy.next


l1 = insert([9,9,9,9,9,9])
l2 = insert([1])

Solution().addTwoNumbers(l1, l2)