class Solution:
    def findMin(self, nums: List[int]) -> int:
        # log n indicates binary search
        # if at any point the left is smaller than mid,
        # min is on the right due to sorted
        # if at any point the left is greater than mid
        # min is on the left due to sorted

        l = 0
        r = len(nums) - 1
        minimum = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                minimum = min(minimum, nums[l])
            mid = (l + r) // 2

            minimum = min(minimum, nums[mid])

            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return minimum

