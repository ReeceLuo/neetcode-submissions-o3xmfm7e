# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # valid - every node in left subtree is smaller, every node in
        # right subtree is larger
        # just checking parent is not enough

        def dfs(node, leftBound, rightBound):
            if not node:
                return True
            if node.val <= leftBound or node.val >= rightBound:
                return False
            
            left = dfs(node.left, leftBound, node.val)
            right = dfs(node.right, node.val, rightBound)
            return left and right
        
        return dfs(root, float("-inf"), float("inf"))
        