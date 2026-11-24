# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(node):
            nonlocal res
            if node is None:
                return 0
            lh, rh = dfs(node.left),  dfs(node.right)
            res = res and -1 <= lh - rh <= 1
            return 1 + max(lh, rh)
        dfs(root)
        return res