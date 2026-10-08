class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # strategy - find whether target is in rotated or
        # unrotated portion, then do binary search
        

        l, r = 0, len(nums) - 1
        
        def bin_search(l, r):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid
            return -1
        
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        res = bin_search(0, l - 1)
        if res != -1:
            return res
        
        return bin_search(l, len(nums) - 1)