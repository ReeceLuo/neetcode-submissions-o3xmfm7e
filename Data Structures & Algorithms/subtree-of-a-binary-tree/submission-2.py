# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def equal(self, p, q):
        if (p and not q) or (q and not p):
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False
        
        left = self.equal(p.left, q.left)
        right = self.equal(p.right, q.right)

        return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # check if subroot is a subtree of root
        # check for equality for each node in root
        if not root and subRoot:
            return False
        if self.equal(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        
        return left or right
        


        