# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # brute force - add all elements to a list, sort, find kth
        # instead add to a heap
        self.heap = []
        def add(self, node):
            if not node:
                return
            heapq.heappush(self.heap, -(node.val))
            if len(self.heap) > k:
                heapq.heappop(self.heap)
            add(self, node.left)
            add(self, node.right)
            return
        add(self, root)
        return -(self.heap[0]) if self.heap else 0
        
