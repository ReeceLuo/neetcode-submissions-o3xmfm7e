class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProf = 0

        p1 = 0
        p2 = 1

        # minVal = prices[0]
        profit = 0
        while p2 <= len(prices) - 1:
            if prices[p2] < prices[p1]:
                p1 = p2
                p2 += 1
            else:
                profit = prices[p2] - prices[p1]
                maxProf = max(maxProf, profit)
                p2 += 1

        return maxProf
