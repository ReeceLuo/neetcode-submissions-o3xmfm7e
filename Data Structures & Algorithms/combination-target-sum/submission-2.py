class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:  

        # base case
        # choice (decision tree)
        # constraints
        # backtracking

        res = []

        def dfs(i, currSum, curr):
            if currSum == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or currSum > target:
                return
            
            curr.append(nums[i])
            dfs(i, currSum + nums[i], curr)

            curr.pop()
            dfs(i + 1, currSum, curr)

        dfs(0, 0, [])
        return res