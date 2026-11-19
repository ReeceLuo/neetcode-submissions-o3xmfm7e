class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        

        l, r = 0, len(nums) - 1
        recent = None
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
                recent = m
            elif nums[m] < target:
                l = m + 1
                recent = l
            else:
                return m
        return recent
        