class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Notes:
            # same number can be chosen unlimited number of times
            # return any order
            # distinct nums

        # edge cases:
            # do not use first num

        res = []

        def dfs(i, curr, currSum):
            if currSum == target:
                res.append(curr.copy())
                return
            if currSum > target or i >= len(nums):
                return
            
            curr.append(nums[i])
            dfs(i, curr, currSum + nums[i])

            curr.pop()
            dfs(i + 1, curr, currSum)

        dfs(0, [], 0)
        return res



        