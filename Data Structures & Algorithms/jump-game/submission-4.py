class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # if you can jump to a higher weight, do it
        # given jump length
        p = 0
        while p < len(nums):
            num = nums[p]
            remaining = num
            for i in range(num):
                p += 1
                remaining -= 1
                if p < len(nums) and nums[p] >= remaining:
                    break
            if p >= len(nums) - 1:
                return True
            if num == 0:
                return False

        return False
