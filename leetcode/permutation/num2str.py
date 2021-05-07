class Solution:

    def letterCombinations(self, digits: str):
        num_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        def recrusive(head, digits):
            if not digits:
                res.append(head[:])
                return
            for ch in num_map[digits[0]]:
                recrusive(head+ch, digits[1:])
        recrusive("", digits)
        return res
    

print(Solution().letterCombinations("23"))