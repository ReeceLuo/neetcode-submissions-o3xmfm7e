class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                minNum = min(minNum, nums[l])
                break
            
            m = (l + r) // 2
            minNum = min(minNum, nums[m])

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1

        # [5, 1, 2, 3, 4]

        return minNum