# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def helper(root) -> int:
            nonlocal res
            if not root:
                return 0
            left = max(helper(root.left), 0)
            right = max(helper(root.right), 0)
            res = max(res, left + right + root.val)
            return root.val + max(left, right)
        helper(root)
        return res