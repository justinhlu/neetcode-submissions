class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = 101
        for i in range(len(prices)):
            if prices[i] < minBuy:
                minBuy = prices[i]
            
            profit = prices[i] - minBuy

            maxProfit = max(maxProfit, profit)

        return maxProfit