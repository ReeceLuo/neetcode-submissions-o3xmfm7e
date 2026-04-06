class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        postfix = []

        prefixProd = 1
        prefix.append(prefixProd)
        for i in range(1, len(nums)):
            prefixProd *= nums[i - 1]
            prefix.append(prefixProd)

        postfixProd = 1
        postfix.append(postfixProd)
        for i in range(len(nums) - 2, -1, -1):
            postfixProd *= nums[i + 1]
            postfix.insert(0, postfixProd)

        output = []
        for i in range(0, len(nums)):
            output.append(prefix[i] * postfix[i])

        return output
            