class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        sellPrice = 0

        for i in range(len(prices)-1, -1, -1):
            profit = sellPrice - prices[i]

            if profit > maxProfit:
                maxProfit = profit
            if prices[i] > sellPrice:
                sellPrice = prices[i]
            

        return maxProfit