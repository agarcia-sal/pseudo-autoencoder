class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        if n == 1:
            return 0
        hold = float('-inf')
        sold = 0
        rest = 0
        for price in prices:
            new_hold = max(hold, rest - price)
            new_sold = hold + price
            new_rest = max(rest, sold)
            hold = new_hold
            sold = new_sold
            rest = new_rest
        return max(sold, rest)