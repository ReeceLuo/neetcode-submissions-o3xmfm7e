class Solution:
    def findMin(self, nums: List[int]) -> int:
        # given sorted array that is rotated, find min element
        # use binary search

        l, r = 0, len(nums) - 1
        minVal = nums[0]

        while l <= r:
            if nums[l] <= nums[r]:
                minVal = min(minVal, nums[l])
                break
            
            m = (l + r) // 2
            minVal = min(minVal, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return minVal
