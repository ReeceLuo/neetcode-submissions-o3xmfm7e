class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Find start of right subarray and then do binary search

        l, r = 0, len(nums) - 1

        # [3,4,5,6,1,2]

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