import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if num piles = hours, return max of piles

        lower = 1
        upper = max(piles)
        minSpeed = upper
        
        while lower <= upper:
            m = (lower + upper) // 2

            hours = h
            for pile in piles:
                hoursNeeded = math.ceil(pile / m)
                hours -= hoursNeeded
                if hours < 0:
                    break
            
            if hours < 0:
                lower = m + 1
            else:
                upper = m - 1
                minSpeed = m

        return minSpeed



