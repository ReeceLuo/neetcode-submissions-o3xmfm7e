# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.currDiff = 0

        def balanced(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            
            heightLeft = balanced(root.left)
            heightRight = balanced(root.right)

            absDiff = abs(heightLeft - heightRight)
            self.currDiff = max(self.currDiff, absDiff)

            return 1 + max(heightLeft, heightRight)

        balanced(root)
        return self.currDiff <= 1





