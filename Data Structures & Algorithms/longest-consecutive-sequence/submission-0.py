class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 0
        for num in nums:
            length = 0
            if num - 1 not in numSet:
                 i = num
                 while i in numSet:
                    length += 1
                    i += 1
            
            longest = max(longest, length)

        return longest