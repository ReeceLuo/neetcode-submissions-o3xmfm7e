class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # return max water container can store
        # wider will give more water. start at either side
        # can only store up to smaller height
        # change whichever height is smaller

        maxArea = 0

        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            maxArea = max(area, maxArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea
