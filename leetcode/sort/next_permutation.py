class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(li, begin, end):
            i = j = begin
            pivot = li[end - 1]
            while j < end - 1:
                if li[j] < pivot:
                    li[i], li[j] = li[j], li[i]
                    i += 1
                j += 1
            li[end - 1], li[i] = li[i], li[end-1]
            return i


        def quick_sort(li, begin, end):
            if begin+1 >= end:
                return
            p = partition(li, begin, end)
            quick_sort(li, begin, p)
            quick_sort(li, p+1, end)

        if len(nums) == 1:
            return
        
        k = len(nums) - 2
        while k >= 0:
            if nums[k] > nums[k+1]:
                k -= 1
                continue
            else:
                break
        if k == -1:
            quick_sort(nums, 0, len(nums))
            return
        
        s = k
        pre_v = nums[s]
        quick_sort(nums, s, len(nums))
        m = s+1
        while m <len(nums)-1:
            if nums[m] > pre_v:
                break
            m +=1
        ii = m
        for j in range(m-1, s-1, -1):

            nums[j], nums[ii] = nums[ii], nums[j]
            ii -= 1


s = Solution()
a = [1,2,3,2,1]
print(a)
s.nextPermutation(a)
print(a)
