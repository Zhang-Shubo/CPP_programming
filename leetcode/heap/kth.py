import collections


class PriorityQueue:
    def __init__(self, k):
        self.data = [None]
        self.k = k

    def insert(self, val):
        if len(self.data) < self.k+1:
            k = len(self.data)
            self.data.append(val)
            self.swim(k)
        else:
            if self.data[1][1] > val[1]:
                return
            self.data[1] = val
            self.sink(1)

    def sink(self, k):
        while 2*k <= self.k:
            p = 2*k
            if p < self.k and self.data[p][1] > self.data[p+1][1]:
                p += 1
            if self.data[p][1] > self.data[k][1]:
                break
            self.data[p], self.data[k] = self.data[k], self.data[p]
            k = p

    def swim(self, k):
        while k>1 and self.data[int(k/2)][1] > self.data[k][1]:
            p = int(k/2)
            self.data[p], self.data[k] = self.data[k], self.data[p]
            k = p

class Solution:
    def topKFrequent(self, nums, k):
        counter = collections.Counter(nums)
        pq = PriorityQueue(k)
        for it in counter.items():
            pq.insert(it)
        
        return [i[0] for i in pq.data[1:]]

a = [5,6,6,7,4,1,1,1,2,2,3,3,3,4,4,4,6]
b = 4
Solution().topKFrequent(a, b)
print(0)