class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0

        min_price_one = float('inf')
        min_price_two = float('inf')
        max_profit_one = 0
        max_profit_two = 0

        for price in prices:
            if price < min_price_one:
                min_price_one = price
            if price - min_price_one > max_profit_one:
                max_profit_one = price - min_price_one
            if price - max_profit_one < min_price_two:
                min_price_two = price - max_profit_one
            if price - min_price_two > max_profit_two:
                max_profit_two = price - min_price_two

        return max_profit_two