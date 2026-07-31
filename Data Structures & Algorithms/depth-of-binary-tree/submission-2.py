# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        res = 0
        while stack:
            cur, depth = stack.pop()
            if cur:
                res = max(res, depth)
                stack.append((cur.left, depth + 1))
                stack.append((cur.right, depth + 1))
        return res