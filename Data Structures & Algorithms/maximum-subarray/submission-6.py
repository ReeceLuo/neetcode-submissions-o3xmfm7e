class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # kadane's algorithm
        # if a subarray's sum is ever negative, no point in adding it,
        # so reset the current subarray

        maxSum = nums[0]
        curr = 0

        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            maxSum = max(maxSum, curr)

        return maxSum