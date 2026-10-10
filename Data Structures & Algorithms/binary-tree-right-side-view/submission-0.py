# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # visible from right side:
        # last node on level
        # need way to track all nodes on level
        # level order traversal

        if not root:
            return []

        res = []
        q = deque()
        q.append(root)

        while q:
            latest = None
            for i in range(len(q)):
                node = q.popleft()
                latest = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(latest)

        return res




