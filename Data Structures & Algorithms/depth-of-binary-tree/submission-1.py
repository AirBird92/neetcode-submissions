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
            cur = stack.pop()
            if not cur[0]:
                continue
            res = max(res, cur[1])
            stack.append((cur[0].left, cur[1] + 1))
            stack.append((cur[0].right, cur[1] + 1))
        return res