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

def link_reverse(lnk):
    dummy = ListNode(val=-1)
    dummy.next = lnk
    pre = lnk
    p_cur = pre.next
    while p_cur:
        # 将下一个节点存储在pre.next里面，直到pre.next为空
        pre.next = p_cur.next
        # 反转链表
        p_cur.next = dummy.next
        dummy.next = p_cur
        # 将下一个节点重新赋值给p_cur
        p_cur = pre.next
    return dummy.next

def link_reverse2(lnk):
    temp = None
    pre = lnk
    while pre:
        next_one = pre.next
        pre.next = temp
        temp = pre
        pre = next_one
    return temp


a = insert([1,2,3,4])

b = link_reverse2(a)
print(0)



