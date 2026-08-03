# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if (len(preorder) == 1):
            return TreeNode(preorder[0])
        
        def helper(preorder, inorder, left, right):
            nonlocal cur, indexMap
            if left > right:
                return None
            root = TreeNode(preorder[cur])
            cur += 1
            mid = indexMap[root.val]
            root.left = helper(preorder, inorder, left, mid - 1)
            root.right = helper(preorder, inorder, mid + 1, right)
            return root
        
        indexMap = {}
        for i in range(len(inorder)):
            indexMap[inorder[i]] = i
        cur = 0
        return helper(preorder, inorder, 0, len(inorder) - 1)