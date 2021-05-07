class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if len(postorder) <= 2:
            return True
        head = postorder[-1]
        i = 0
        while postorder[i] < head: i += 1
        j = i
        while postorder[j] > head: j += 1
        if j < len(postorder) - 1:
            return False
        return self.verifyPostorder(postorder[0:i]) and self.verifyPostorder(postorder[i:-1])


Solution().verifyPostorder([1,2,3,4,5])