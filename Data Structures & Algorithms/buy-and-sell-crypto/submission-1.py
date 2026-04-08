class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # brute force - for each day, scan until end and track max

        currMax = 0
        for i, val in enumerate(prices):
            for j in range (i + 1, len(prices)):
                if prices[j] - val > currMax:
                    currMax = prices[j] - val

        return currMax