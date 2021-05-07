# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        link_group = []
        link_group_head = []
        p = head
        i = k
        while p and i>0:
            link_group.append(p)
            link_group_head.append(p)
            p = p.next
            i -= 1
        if i > 0:
            return head
        i = k
        last = p
        while p:
            q = p
            while q and i > 0:
                q = q.next
                i -= 1
            if i == 0:
                for j in range(k):
                    link_group[j].next = p
                    link_group[j] = p
                    p = p.next
                last = q
                i = k
            else:
                last = p
                break
        for z in link_group:
            z.next = None
        p = head = None
        while True:
            if link_group_head[0] is None:
                break
            for u in range(k):
                node = link_group_head[k-u-1]
                if not p:
                    p = head = node
                    link_group_head[k-u-1] = node.next
                    continue
                p.next = node
                link_group_head[k-u-1] = node.next
                p = p.next
    
        p.next = last
        return head

    def reverse(self, head):
        dummy = ListNode(-1)
        p_pre = head
        dummy.next = head
        p_cur = head.next
        while p_cur:
            p_pre.next = p_cur.next
            p_cur.next = dummy.next
            dummy.next = p_cur
            p_cur = p_pre.next
        return dummy.next, p_pre

    def reverseKGroup2(self, head: ListNode, k: int) -> ListNode:
        last_tail = tail = head
        pre = head
        dummy = ListNode(-1)
        dummy.next = head
        i = 0
        while True:

            for j in range(k-1):
                
                if not tail:
                    break
                tail = tail.next
                
            if not tail:
                break
            next_one = tail.next
            tail.next = None
            head, tail = self.reverse(pre)
            last_tail.next = head
            last_tail = tail
            tail.next = next_one
            pre = next_one
            tail = next_one
            
            if i == 0:
                dummy.next = head
            i += 1


        
        
        return dummy.next


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


h = insert([1,2,3,4,5, 6])
a = Solution()
b = a.reverseKGroup2(h, 3)
print(0)

        


