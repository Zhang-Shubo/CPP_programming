# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def recrusive(root):
            if not root:
                return
            res.append(root.val)
            recrusive(root.left)
            recrusive(root.right)
        recrusive(root)
        return res
    
    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = []
        cur = root
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            cur = stack.pop()
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def recrusive(root):
            if not root:
                return
            recrusive(root.left)
            res.append(root.val)
            recrusive(root.right)
        recrusive(root)
        return res

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

            
        return res
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def recrusive(root):
            if not root:
                return 
            recrusive(root.left)
            recrusive(root.right)
            res.append(root.val)
        recrusive(root)
        return res

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        curr = root
        prev = None
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
                stack.append
            curr = stack.pop()
            if not curr.right or curr.right == prev:
                res.append(curr.val)
                prev = curr
                curr = None
            else:
                stack.append(curr)
                curr = curr.right
        return res