class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1] * len(nums)

        prefixProd = 1
        postfixProd = 1

        for i in range(len(nums)):
            output[i] = prefixProd
            prefixProd *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfixProd
            postfixProd *= nums[i]

        return output
            