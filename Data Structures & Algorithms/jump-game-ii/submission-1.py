class Solution:
    def jump(self, nums: List[int]) -> int:
        # from each jump, take the max of current jump + new jump

        # 3, 5, 0, 0, 0, 1
        # here, one is the better option even though less than 2
        # need to account for position
        jumps = 0
        l = r = 0

        while r < len(nums) - 1:
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            l = r + 1
            r = furthest
            jumps += 1
        return jumps