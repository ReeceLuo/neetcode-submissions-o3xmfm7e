class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # brute force - check every subarray O(n^2)
        # kardane's algorithm - if at any point a subarray value is
        # negative, reset subarray, as adding to it would be adding
        # a negative value
        # O(n)

        maxSum = nums[0]
        curr = 0
        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            maxSum = max(maxSum, curr)

        return maxSum
        


            