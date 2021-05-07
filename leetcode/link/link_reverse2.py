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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        p = head
        dummy = ListNode(-1)
        dummy.next = head
        last = dummy
        i = 1
        while i < m:
            last = p
            p = p.next
            i += 1
        temp = None
        restart = p
        while i <= n:
            next_one = p.next
            p.next = temp
            temp = p
            p = next_one
            i += 1

        last.next = temp
        restart.next = p
        

        return dummy.next


a = insert([1,2,3,4])

b = Solution().reverseBetween(a, 1,3)
print(0)

