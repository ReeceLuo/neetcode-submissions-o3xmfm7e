# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def diameter(root: Optional[TreeNode]):
            if root is None:
                return 0
            
            heightLeft = diameter(root.left)
            heightRight = diameter(root.right)
            
            self.result = max(self.result, heightLeft + heightRight)
            return 1 + max(heightLeft, heightRight)
        diameter(root)
        return self.result





