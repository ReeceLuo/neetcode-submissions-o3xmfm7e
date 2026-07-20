class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # brute force - use set to track seen nums
        
        # since numbers range from 1 to n, we can use the array indexes
        # as a hashset since it ranges from 0 to n. This does not use
        # O(1) extra space

        # process each value, go to the index the value points to and
        # mark it somehow. here, we can mark it negative. if we ever go to
        # an index (can be from any position in the array) and it is already
        # marked negative, we know we have visited that index from another
        # number in the array, so that index value is the duplicate

        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])
            nums[abs(nums[i]) - 1] *= -1