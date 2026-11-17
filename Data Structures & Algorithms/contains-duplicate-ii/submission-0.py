class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # find whether the array has duplicate values within k indices

        # fixed sliding window

        # edge cases:
            # k = 0
            # k = 1
            # k > len(nums)

        if k == 0:
            return False
        
        # use dictionary to track letters

        counts = {}
        for i in range(0, min(k, len(nums))):
            if nums[i] in counts:
                return True
            counts[nums[i]] = counts.get(nums[i], 0) + 1
        
        i, j = 0, k
        while j < len(nums):
            if nums[j] in counts:
                return True
            counts[nums[j]] = counts.get(nums[j], 0) + 1
            j += 1
            counts[nums[i]] -= 1
            if counts[nums[i]] == 0:
                del counts[nums[i]]
            i += 1
        return False









