class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # base case
        # choice (decision tree) - include a number and move on or exclude a number and move on
        # constraints - no duplicate subsets
        # backtracking



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