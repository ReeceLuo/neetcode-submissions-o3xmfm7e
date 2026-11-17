class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # choose lowest day to buy

        j = 0
        buy = prices[0]
        maxProf = 0
        while j < len(prices):
            if prices[j] < buy:
                buy = prices[j]
            maxProf = max(maxProf, prices[j] - buy)
            j += 1

        return maxProf
