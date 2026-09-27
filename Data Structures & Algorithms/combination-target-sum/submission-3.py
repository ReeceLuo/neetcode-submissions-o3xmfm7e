class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # all unique combintations - explore all possible valid options,
        # which indicates backtracking
            # base case - when to stop exploring
            # choice - what decision do we make
            # constraints
            # backtracking

        res = []

        def dfs(curr, currSum, i):
            if currSum == target:
                res.append(curr.copy())
                return
            if currSum > target or i >= len(nums):
                return
            
            curr.append(nums[i])
            dfs(curr, currSum + nums[i], i)

            curr.pop()
            dfs(curr, currSum, i + 1)

        dfs([], 0, 0)
        return res
        