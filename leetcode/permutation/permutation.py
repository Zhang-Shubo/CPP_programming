import copy
res = []


def is_swap(data):
    if len(data) >= 1:
        if data[-1] in data[:-1]:
            return False
    return True


def recrusive(data_list, start, end):
    if start == end:
        res.append(data_list)
        return
    else:
        for i in range(start, end):
            data_copy = copy.deepcopy(data_list)
            if is_swap(data_copy[start:i+1]):
                data_copy[i], data_copy[start] = data_copy[start], data_copy[i]

                recrusive(data_copy, start+1, end)

def permutation(data_list):


    recrusive(data_list, 0, len(data_list))


class Solution:

    def permute(self, nums):
        res = []

        def recrusive2(nums, start):
            if start>=len(nums):
                res.append(nums[:])
                return
            for i in range(start, len(nums)):
                new = copy.copy(nums)
                new[i], new[start] = new[start], new[i]
                recrusive(new, start+1)

        def recrusive(nums, start):
            if start>=len(nums):
                res.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                recrusive(nums, start+1)
                nums[start], nums[i] = nums[i], nums[start]
        recrusive2(nums, 0)
        return res

res = Solution().permute([1, 2, 3])

print(res)