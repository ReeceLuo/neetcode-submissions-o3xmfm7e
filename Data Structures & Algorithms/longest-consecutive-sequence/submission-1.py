class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # consecutive sequence - each element is one greater than prev
        # we have to start tracking from the first in sequence
        # a value n is a first in sequence if n - 1 is NOT in nums
        
        numSet = set(nums)

        maxLength = 0
        for num in nums:
            count = 0
            if num - 1 in numSet:
                continue
            # not in numset, so start of sequence
            while num in numSet:
                count += 1
                num += 1
            maxLength = max(maxLength, count)

        return maxLength
