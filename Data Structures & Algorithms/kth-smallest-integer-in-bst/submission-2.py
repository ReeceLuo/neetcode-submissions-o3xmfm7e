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
        # using heap if k is small:
            # heapifying and then popping k times - O(n) heapify 
            # and then popping k times O(klogn), which is O(n)
            #  
        self.nums = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.nums.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return self.nums[k - 1]
        

