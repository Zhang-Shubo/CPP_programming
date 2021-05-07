class Solution:
    def quick_sort(self, intervals):
        def partition(data, start, end):
            pivot = end - 1
            i, j = start, start
            while i < end - 1:
                if data[i] < data[pivot]:
                    data[i], data[j] = data[j], data[i]
                    j += 1
                i += 1
            data[pivot], data[j] = data[j], data[pivot]
            return j

        def recursive(data, start, end):
            if start >= end - 1:
                return
            p = partition(data, start, end)
            recursive(data, start, p)
            recursive(data, p+1, end)
        
        recursive(intervals, 0, len(intervals))

    def merge(self, intervals):
        self.quick_sort(intervals)
        res = [intervals[0]]
        for tup in intervals[1:]:
            if tup[0] < res[-1][1]:
                res[-1] = [res[-1][1] if res[-1][1] > tup[1] else tup[1]]
            else:
                res.append(tup)

        return res


a = [[1,3],[2,6],[8,10],[15,18]]

b = Solution().merge(a)