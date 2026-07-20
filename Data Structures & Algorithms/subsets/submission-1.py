class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking - keep trying a solution until it is no longer valid,
        # backtrack to the most recent valid position

        # num subsets = 2 ^ len(nums)
        res = []
        
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res