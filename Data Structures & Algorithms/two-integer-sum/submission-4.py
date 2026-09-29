class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return indices i and j such that nums[i] + nums[j] == target
        # every input has solution
        indices = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in indices:
                return [indices[complement], i]
            indices[num] = i

        return [] 
