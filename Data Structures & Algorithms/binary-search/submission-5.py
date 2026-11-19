class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # brute force - linear time
        # O(log n) - binary search

        # edge cases:
            # last number
            # first number
            # does not exist

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        return -1