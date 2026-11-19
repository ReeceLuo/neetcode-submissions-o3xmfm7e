class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # notes:
            # h is amount of time
            # speed does not carry over to next pile
            # find min eating speed to still finish in k

        # edge cases:
            # eating speed of 1
            # eating speed of max(pile)
        
        l, r = 1, max(piles)

        minSpeed = max(piles)
        while l <= r:
            speed = (l + r) // 2

            time = 0
            for pile in piles:
                time += math.ceil(pile / speed)
            
            if time > h:
                l = speed + 1
            else:
                minSpeed = min(minSpeed, speed)
                r = speed - 1

        return minSpeed


