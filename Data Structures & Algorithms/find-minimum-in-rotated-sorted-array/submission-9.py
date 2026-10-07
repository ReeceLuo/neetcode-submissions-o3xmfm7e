class Solution:
    def findMin(self, nums: List[int]) -> int:
        # given sorted array that is rotated, find min element
        # use binary search

        l, r = 0, len(nums) - 1
        minVal = nums[0]

        while l <= r:
            if nums[l] < nums[r]: # no rotations remaining
                minVal = min(minVal, nums[l])
                break

            mid = (r + l) // 2
            minVal = min(minVal, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return minVal

        # [5, 0, 1, 2, 3, 4]
