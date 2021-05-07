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
        stack1 = []
        stack2 = []
        p1, p2 = l1, l2
        while p1:
            stack1.append(p1.val)
            p1 = p1.next
        while p2:
            stack2.append(p2.val)
            p2 = p2.next
        p = l = None
        up = 0
        mod = 0
        while stack1 or stack2:
            mod = ((stack1.pop() if stack1 else 0) + (stack2.pop() if stack2 else 0) + up) % 10
            up = ((stack1.pop() if stack1 else 0) + (stack2.pop() if stack2 else 0) + up) // 10
            l = ListNode(mod)
            l.next = p
            p = l

        if up:
            l = ListNode(up)
            l.next = p
        return l


l1 = insert([9,9,9,9,9,9])
l2 = insert([1])

Solution().addTwoNumbers(l1, l2)