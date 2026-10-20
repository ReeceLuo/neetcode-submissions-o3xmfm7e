class Solution:
    def jump(self, nums: List[int]) -> int:
        # set indices that can be reached by a jump is a "level"
        # any indicie in each level can get to the next
        
        # starting from first indice, map out range of indices
        # we can reach from it
            # this range is determined by largest distance reachable
        # then, go through this range to get next range

        # l: 2
        # r: 5
        jumps = 0
        l = r = 0
        while r < len(nums) - 1:
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            
            l = r
            r = furthest
            jumps += 1
        
        return jumps
    

