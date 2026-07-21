class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # base case - when the index is out of range, stop exploring
        # decision - include each number or exclude. but duplicates
        # will lead to repeat subsets
        # sort and group duplicates together

        res = []

        nums.sort()

        def dfs(i, curr):
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            dfs(j, curr)
        
        dfs(0, [])
        return res



