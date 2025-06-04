class Solution(object):
    def maxProfit(self, prices):
        profit = 0 
        minimum = prices[0]
        for i in range(len(prices)):
            cost = prices[i]- minimum
            profit = max(profit,cost)
            minimum = min(minimum,prices[i])
            i+=1
        return profit
        