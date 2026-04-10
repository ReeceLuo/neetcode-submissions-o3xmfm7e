import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if num piles = hours, return max of piles
        # upper bound - max(piles) if h >= num piles
        # lower bound - 1

        l = 1
        r = max(piles)
        minSpeed = r
        
        if len(piles) == h:
            return r

        while l <= r:
            m = (l + r) // 2

            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile / m)
            
            if totalHours <= h:
                minSpeed = m
                r = m - 1
            else:
                l = m + 1
        
        return minSpeed



