class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # create array of 2x length

        nums.extend(nums)
        return nums