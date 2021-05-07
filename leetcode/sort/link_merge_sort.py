
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Link:

    def __init__(self):
        self.root = Node(None)
        self.end = self.root

    def insert(self, data):
        if isinstance(data, list):
            for d in data:
                self.insert(d)
            return

        n = Node(data)
        self.end.next = n
        self.end = n


def merge(l_link, r_link):
    lp = l_link.root
    rp = r_link.root
    link = Link()
    p = link.root
    while lp.next and rp.next:
        if lp.next.value < rp.next.value:
            p.next = Node(lp.next.value)
            lp = lp.next
        else:
            p.next = Node(rp.next.value)
            rp = rp.next
        p = p.next
    while lp.next:
        p.next = Node(lp.next.value)
        lp = lp.next
        p = p.next

    while rp.next:
        p.next = Node(rp.next.value)
        rp = rp.next
        p = p.next
    
    return link


def merge_no_copy(l_link, r_link):
    """总是循环引用"""
    lp = l_link.root
    rp = r_link.root
    link = Link()
    p = link.root
    while lp.next and rp.next:
        if lp.next.value < rp.next.value:
            p.next = lp.next
            lp = lp.next
        else:
            p.next = rp.next
            rp = rp.next
        p = p.next
    while lp.next:
        p.next = lp.next
        lp = lp.next
        p = p.next

    while rp.next:
        p.next = rp.next
        rp = rp.next
        p = p.next
    
    return link


def merge_sort(link):
    if not link.root.next or not link.root.next.next:
        return link
    l_link = Link()
    r_link = Link()
    p = link.root.next
    lp = l_link.root
    rp = r_link.root
    while p:
        lp.next = p
        lp = lp.next
        p = p.next
        if not p:
            rp.next = None
            break
        
        rp.next = p
        rp = rp.next
        p = p.next
        if not p:
            lp.next = None
    sorted_l_link = merge_sort(l_link)
    sorted_r_link = merge_sort(r_link)

    return merge(sorted_l_link, sorted_r_link)


def merge_sort_center(link):
    if not link.root.next or not link.root.next.next:
        return link
    slower = link.root.next
    faster = link.root.next.next
    while faster:
        faster = faster.next
        if not faster:
            break
        faster = faster.next
        slower = slower.next
    
    r_link = Link()
    r_link.root.next = slower.next
    slower.next = None
    sorted_l_link = merge_sort(link)
    sorted_r_link = merge_sort(r_link)

    return merge(sorted_l_link, sorted_r_link)



l = Link()
l.insert([1,7,3,9,10,20,33,5,8,4])

ll = merge_sort_center(l)
print(ll)