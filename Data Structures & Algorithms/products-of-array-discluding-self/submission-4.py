class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # no division operator
        # product is product of all numbers before and all numbers after

        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            prefix[i] *= pre
            pre *= nums[i]
        
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] *= post
            post *= nums[i]
        
        for i in range(len(nums)):
            nums[i] = prefix[i] * postfix[i]

        return nums