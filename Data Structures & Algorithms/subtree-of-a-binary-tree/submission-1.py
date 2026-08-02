# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False

        def sameTree(n1, n2) -> bool:
            if n1 is None or n2 is None:
                return n1 == n2
            return n1.val == n2.val and sameTree(n1.left, n2.left) and sameTree(n1.right, n2.right)
        
        if root.val == subRoot.val and sameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)