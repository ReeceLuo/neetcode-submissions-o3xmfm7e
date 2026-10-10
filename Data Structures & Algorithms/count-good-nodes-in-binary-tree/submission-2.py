# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # good: must be >= than root
        # no larger nodes between node and root
        
        # as we explore subtrees, track max upper bound
        if not root:
            return 0

        self.count = 0
    
        def dfs(node, upperBound):
            if not node:
                return
            if node.val >= upperBound:
                self.count += 1
                upperBound = node.val
            dfs(node.right, upperBound)
            dfs(node.left, upperBound)

        dfs(root, root.val)
        return self.count







