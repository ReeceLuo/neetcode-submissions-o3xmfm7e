class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # if the complement between the current value and the
        # target is present, then those are the two integers
        # can you hashmap with index

        hashMap = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashMap:
                return [hashMap[complement], i]
            hashMap[num] = i

        return