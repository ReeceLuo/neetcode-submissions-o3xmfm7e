class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking - keep trying a solution until it is no longer valid,
        # backtrack to the most recent valid position

        # num subsets = 2 ^ len(nums)
        # decision tree: at each element, we either include or exclude
        # 

        res = []

        def dfs(i, curr):
            if i >= len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()
            dfs(i + 1, curr)
        
        dfs(0, [])
        return res



            