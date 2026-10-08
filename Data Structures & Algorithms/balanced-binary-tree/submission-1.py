# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # balanced - if height diff of left / right is 
        # no greater than 1
        # to find height, we need separate method because we
        # need to recursively find int and this method returns 
        # bool
        self.isBalanced = True

        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            if abs(left - right) > 1:
                self.isBalanced = False
            return 1 + max(left, right)
        
        height(root)
        return self.isBalanced

        
