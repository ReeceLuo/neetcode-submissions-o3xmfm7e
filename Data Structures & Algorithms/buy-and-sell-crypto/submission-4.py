class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of max profit
        # keep track of when to buy
            # slide right pointer to right 


        maxProf = 0

        buy = prices[0]

        for price in prices:
            if price < buy:
                buy = price
                continue
            
            profit = price - buy
            maxProf = max(maxProf, profit)

        return maxProf