class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # base case
        # choice - add a number or move on
        # constraint - must contain all numbers. If we move past a number
        # we should add it again
        # backtracking - once a number is added, remove it


        res = []

        added = [False] * len(nums)

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if added[i] == False:
                    curr.append(nums[i])
                    added[i] = True
                    dfs(curr)
                    curr.pop()
                    added[i] = False

        dfs([])
        return res

