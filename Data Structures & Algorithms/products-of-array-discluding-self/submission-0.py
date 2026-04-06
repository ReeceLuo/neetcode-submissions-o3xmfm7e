class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []

        for i in range(0, len(nums)):
            productWithout = 1

            for j in range(0, len(nums)):
                if i == j:
                    continue
                else:
                    productWithout *= nums[j]

            output.append(productWithout)
        
        return output