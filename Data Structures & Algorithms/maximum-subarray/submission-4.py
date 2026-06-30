class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # brute force - check every subarray 
        maxSum = nums[0]

        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr += nums[j]
                maxSum = max(maxSum, curr)
        
        return maxSum
        


            