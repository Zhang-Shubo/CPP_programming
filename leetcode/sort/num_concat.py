class Solution:
    def minNumber(self, nums) -> str:
        nums = list(map(str, nums))
        def less(val1,val2):
            if val1 == val2:
                return False
            l1 = len(val1)
            l2 = len(val2)
            if l1<l2:
                return not less(val2, val1)
            i = 0
            while i<l1:
                if int(val1[i]) < float(val2[i] if i <l2 else 0.5):
                    return True
                elif int(val1[i]) > float(val2[i] if i <l2 else 0.5):
                    return False

                i += 1
            return False


        def partition(nums, start, end):
            pivot = end - 1
            i, j = start, start
            while i<end-start-1:
                if less(nums[i], nums[pivot]):
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
                i += 1
            nums[pivot], nums[j] = nums[j], nums[pivot]
            return j

        def recursive(nums, start, end):
            if start + 1 >= end:
                return

            p = partition(nums, start, end)
            recursive(nums, start, p)
            recursive(nums, p+1, end)
        
        recursive(nums, 0, len(nums))
        return "".join(nums)


Solution().minNumber([1,2,10,4,40,0])
