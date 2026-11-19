class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # strategy - find two subarrays. do binary searhc on each

        def bin_search(l, r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m
            return -1

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        
        # [4, 5, 6, 7, 0, 1, 2]
        res = bin_search(0, l - 1)
        if res != -1:
            return res
        return bin_search(l, len(nums) - 1)

        


        

        