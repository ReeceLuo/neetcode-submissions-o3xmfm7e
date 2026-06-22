class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # brute force - check every subarray
        # use dynamic programming

        max_sum = nums[0]

        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i + 1, len(nums)):
                curr += nums[j]
                max_sum = max(max_sum, curr)
            max_sum = max(max_sum, curr)

        return max_sum


            