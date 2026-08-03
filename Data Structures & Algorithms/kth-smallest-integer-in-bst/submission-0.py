# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = k
        def inorder(root):
            nonlocal counter
            if not root:
                return None
            
            temp = inorder(root.left)
            if counter == 0 and temp:
                return temp
            counter -= 1
            if counter == 0:
                return root.val
            temp = inorder(root.right)
            if counter == 0 and temp:
                return temp
            return None
        res = inorder(root)
        return res if res else -1
            