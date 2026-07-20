class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking - keep trying a solution until it is no longer valid,
        # backtrack to the most recent valid position

        # num subsets = 2 ^ len(nums)
        res = [[]]
        
        # for each subset, one include nad one exclude

        for num in nums:
            res += [subset + [num] for subset in res]

        return res