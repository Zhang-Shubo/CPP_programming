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
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head and head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        cur = head.next
        p = head
        while cur:
            if cur.val >= p.val:
                p = p.next
            else:
                temp = dummy
                while temp.next.val <= cur.val:
                    temp = temp.next
                p.next = cur.next
                cur.next = temp.next
                temp.next = cur
            cur = p.next

        return dummy.next   


a = insert([2,3,1,4,5,1,2])

b = Solution().insertionSortList(a)
print(0)