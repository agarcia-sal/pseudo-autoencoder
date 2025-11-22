from math import inf

class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        n = len(prices)
        if n == 1:
            return 0
        hold = -inf
        sold = 0
        rest = 0
        for price in prices:
            new_hold = max(hold, rest - price)
            new_sold = hold + price
            new_rest = max(rest, sold)
            hold, sold, rest = new_hold, new_sold, new_rest
        return max(sold, rest)