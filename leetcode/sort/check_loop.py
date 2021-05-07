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


a = Link()
a.insert([1,4,2,8,11,23,12,4,6,3,7])


a.end.next = a.root.next.next


def check_loop(l):
    if not l.root.next or not l.root.next.next:
        return None
    
    faster = l.root.next.next
    slower = l.root.next

    while faster:
        faster = faster.next
        if not faster:
            break
        faster = faster.next
        slower = slower.next

        if faster == slower:
            return faster
    return None


def get_loop_head(l):

    meet = check_loop(l)
    if not meet:
        return None
    p = l.root
    while meet != p:
        meet = meet.next
        p = p.next
    return p


print(get_loop_head(a).value)