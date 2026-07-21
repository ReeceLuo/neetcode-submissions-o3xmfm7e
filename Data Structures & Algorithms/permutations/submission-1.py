class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        # base case - every num added = stop exploring
        # i >= len(nums) = stop exploring

        # choice - not exactly include/exclude
        # iterate through all numbers each time
        # if included, mark as such. do this until all numbers added
        added = [False] * len(nums)

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if not added[i]:
                    curr.append(nums[i])
                    added[i] = True
                    dfs(curr)
                    curr.pop()
                    added[i] = False

        dfs([])
        return res
