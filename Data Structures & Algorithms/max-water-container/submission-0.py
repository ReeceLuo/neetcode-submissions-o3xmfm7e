class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxWater = 0

        l = 0
        r = len(heights) - 1

        while (l < r):
            height = min(heights[l], heights[r])
            waterAmount = height * (r - l)

            if waterAmount > maxWater:
                maxWater = waterAmount

            if heights[l] > heights[r]:
                r -= 1
            else:
                l +=1

        return maxWater
