class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # kadane's algorithm
        # even if an element is negative, if the total subarray is still
        # positive then it is still optimal to add it
        # if a subarray's sum is ever negative, no point in adding it,
        # so reset the current subarray

        maxSum = nums[0]
        currSum = 0
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSum = max(maxSum, currSum)
        
        return maxSum
        