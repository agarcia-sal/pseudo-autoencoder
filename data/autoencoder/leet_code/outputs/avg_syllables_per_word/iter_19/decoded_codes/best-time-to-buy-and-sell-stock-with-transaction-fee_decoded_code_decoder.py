class Solution:
    def maxProfit(self, prices, fee):
        cash = 0
        hold = float('-inf')
        for price in prices:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)
        return cash