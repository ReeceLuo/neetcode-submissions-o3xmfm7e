class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # strategy - find whether target is in rotated or
        # unrotated portion, then do binary search
        

        l, r = 0, len(nums) - 1
        minVal = nums[0]
        minIndex = 0

        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < minVal:
                    minIndex = l
                break
            
            mid = (l + r) // 2
            if nums[mid] < minVal:
                minVal = nums[mid]
                minIndex = mid

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        l, r = 0, len(nums) - 1
        if target > nums[r]:     # in rotated portion
            r = minIndex - 1
        elif target < nums[r]:   # in unrotated portion
            l = minIndex
        else:
            return r
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        
        return -1



            