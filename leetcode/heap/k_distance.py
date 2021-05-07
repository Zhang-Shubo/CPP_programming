import math
dis = {}

def less(p1, p2):
    d1 = dis.get(tuple(p1))
    if not d1:
        d1 = math.sqrt(p1[0]**2+p1[1]**2)
        dis[tuple(p1)] = d1

    d2 = dis.get(tuple(p2))
    if not d2:
        d2 = math.sqrt(p2[0]**2+p2[1]**2)
        dis[tuple(p2)] = d2
    return d1 < d2

class PriorityQueue:
    def __init__(self, k):
        self.k = k
        self.data = [None]

    def insert(self, val):
        k = len(self.data)
        if k < self.k + 1:
            self.data.append(val)
            self.swim(k)
        else:
            if less(val, self.data[1]):
                self.data[1] = val
                self.sink(1)

    def swim(self, k):
        while k > 1 and less(self.data[int(k/2)], self.data[k]):
            self.data[int(k/2)], self.data[k] = self.data[k], self.data[int(k/2)]
            k = int(k/2)

    def sink(self, k):
        while 2*k <= self.k:
            j = 2*k
            if j < self.k and less(self.data[j], self.data[j+1]):
                j += 1
            if less(self.data[j], self.data[k]):
                break
            self.data[k], self.data[j] = self.data[j], self.data[k]
            k = j
            

class Solution:

    def kClosest(self, points, k):
        pq = PriorityQueue(k)
        for p in points:
            pq.insert(p)
        
        return pq.data[1:]


a = [[1,3],[5,5],[-2,2]]
b = 2

sol
        