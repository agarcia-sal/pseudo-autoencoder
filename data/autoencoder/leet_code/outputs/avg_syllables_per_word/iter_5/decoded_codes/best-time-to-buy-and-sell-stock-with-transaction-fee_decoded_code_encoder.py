class Solution:
    def maxProfit(self, prices, fee):
        cash, hold = 0, float('-inf')
        for price in prices:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)
        return cash