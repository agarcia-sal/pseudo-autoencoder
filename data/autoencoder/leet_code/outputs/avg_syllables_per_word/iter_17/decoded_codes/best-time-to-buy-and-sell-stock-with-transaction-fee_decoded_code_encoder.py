from math import inf

class Solution:
    def maxProfit(self, prices, fee):
        cash = 0
        hold = -inf
        for price in prices:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)
        return cash