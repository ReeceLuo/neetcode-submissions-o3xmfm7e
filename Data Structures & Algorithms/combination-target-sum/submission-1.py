class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # decision tree - at each number, include if possible
        # include or exclude
        # 
        # BACKTRACKING TEMPLATE
        # base case
        # choices (decision tree)
        # constraints
        # backtracking step

        res = []

        def dfs(i, curr, currSum):
            if currSum == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or currSum > target:
                return
            
            curr.append(nums[i])
            dfs(i, curr, currSum + nums[i])
            curr.pop()
            dfs(i + 1, curr, currSum)

        dfs(0, [], 0)
        return res