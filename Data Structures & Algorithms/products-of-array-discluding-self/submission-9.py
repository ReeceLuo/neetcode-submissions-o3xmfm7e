class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # w/ division operator: find total product, divide by
        # curr element for each index

        # prefix / postfix product
        # product of all elements but itself is product of prefix before
        # and postfix after
            # [prefix * i * postfix]

        # O(n) scan to calculate each

        output = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output

        # 1, 1, 2, 8
        # 48, 24, 6, 1



