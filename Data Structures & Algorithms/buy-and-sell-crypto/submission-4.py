class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        sellPrice = 0

        for i in range(len(prices)-1,-1,-1):
            sellPrice = max(sellPrice, prices[i])
            profit = sellPrice - prices[i]
            maxProfit = max(profit, maxProfit)
        
        return maxProfit