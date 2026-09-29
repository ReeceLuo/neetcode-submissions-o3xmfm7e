class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # return array where each index is the product of values at
        # all other indexes

        # brute force - for each element (n elements), scan all other
        # elements and take product: O(n^2)

        # observation - product = product of all before and all after
        output = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            output[i] *= pre
            pre *= nums[i]

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= post
            post *= nums[i]
        
        return output



