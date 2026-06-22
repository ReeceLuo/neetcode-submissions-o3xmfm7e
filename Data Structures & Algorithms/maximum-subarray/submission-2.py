class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # brute force - check every subarray
        # use dynamic programming
        # Kadane's algorithm

        maxSum = nums[0]
        curSum = 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSum = max(maxSum, curSum)
        return maxSum


        


            