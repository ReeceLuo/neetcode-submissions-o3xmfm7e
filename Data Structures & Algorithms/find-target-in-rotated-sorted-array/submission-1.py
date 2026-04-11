class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Goal - search for target value
        # two natural subarrays
            # Run binary search on both subarrays

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        def binarySearch(l, r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1

            return -1

        result1 = binarySearch(0, l - 1)
        if result1 != -1:
            return result1
        
        return binarySearch(l, len(nums) - 1)
        