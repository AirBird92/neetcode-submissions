# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur is None:
                continue
            cur.left, cur.right = cur.right, cur.left
            stack.append(cur.right)
            stack.append(cur.left)
        return root