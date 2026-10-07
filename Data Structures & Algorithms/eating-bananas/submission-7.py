class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # given list of banana piles
        # max one pile per hour
        # find min eating speed that you can have to finish all
        # bananas in h given hours

        l, r = 1, max(piles)
        minSpeed = r

        while l <= r:
            mid = int((l + r) / 2)
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)

            if time <= h: # can eat in time
                minSpeed = min(minSpeed, mid)
                r = mid - 1
            else: # can't eat in time
                l = mid + 1

        return minSpeed