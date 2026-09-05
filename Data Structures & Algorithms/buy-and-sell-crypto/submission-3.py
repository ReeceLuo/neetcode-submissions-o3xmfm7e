class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find max profit - largest difference between a price
        # and a price that comes after

        # brute force - nested loop, for each price, get difference of price after and track max
        # better - two pointer

        l, r = 0, 0
        maxProf = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            
            profit = prices[r] - prices[l]
            maxProf = max(maxProf, profit)
            r += 1
        
        return maxProf

            


