class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = 101

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            profit = prices[i] - minPrice
            if profit > maxProfit:
                maxProfit = profit
                
        return maxProfit