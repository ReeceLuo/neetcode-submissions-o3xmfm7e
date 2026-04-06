class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []

        prefixProd = 1
        postfixProd = 1

        output.append(prefixProd)
        for i in range(1, len(nums)):
            prefixProd *= nums[i - 1]
            output.append(prefixProd)

        for i in range(len(nums) - 2, -1, -1):
            postfixProd *= nums[i + 1]
            output[i] *= postfixProd

        return output
            