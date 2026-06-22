class Solution:
    def jump(self, nums: List[int]) -> int:
        # from each jump, take the max of current jump + new jump

        # 5, 2, 0, 0, 0, 1
        # here, one is the better option even though less than 2
        # need to account for position
        jumps = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            jumps += 1
        
        return jumps