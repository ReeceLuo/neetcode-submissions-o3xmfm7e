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
        if root is None and subRoot:
            return False
        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        elif root is None:
            return False
        elif subRoot is None:
            return False
        elif root.val != subRoot.val:
            return False

        equalLeft = self.sameTree(root.left, subRoot.left)
        equalRight = self.sameTree(root.right, subRoot.right)

        return equalLeft and equalRight


        

