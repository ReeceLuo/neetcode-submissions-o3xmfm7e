class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # no division operator
        # product is product of all numbers before and all numbers after

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