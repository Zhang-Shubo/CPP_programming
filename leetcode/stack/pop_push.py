class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stack = []
        j = 0
        for value in pushed:
            stack.append(value)
            l = len(stack)
            while l:
                if stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
                    l -= 1
                else:
                    break

        return j == len(popped)

a = [1,2,3,4,5]
b = [4,5,3,2,1]
Solution().validateStackSequences(a, b)