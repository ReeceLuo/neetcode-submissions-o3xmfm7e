class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxWater = 0

        p1 = 0
        p2 = len(heights) - 1

        while p2 > p1:
            water = (p2 - p1) * min(heights[p1], heights[p2])
            maxWater = max(water, maxWater)

            if heights[p1] > heights[p2]:
                p2 -= 1
            else:
                p1 += 1

        return maxWater
