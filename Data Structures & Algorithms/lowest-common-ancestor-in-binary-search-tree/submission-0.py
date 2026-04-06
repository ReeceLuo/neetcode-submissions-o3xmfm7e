# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # if either p or q equal the root, then they have to be lca
        if p.val == root.val or q.val == root.val:
            return root

        # if p and q are in left/right subtrees, root has to be lca
        if p.val < root.val and q.val > root.val:
            return root
        if p.val > root.val and q.val < root.val:
            return root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)

