class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        min_price1 = float('inf')
        min_price2 = float('inf')
        max_profit1 = 0
        max_profit2 = 0
        for price in prices:
            if price < min_price1:
                min_price1 = price
            if price - min_price1 > max_profit1:
                max_profit1 = price - min_price1
            if price - max_profit1 < min_price2:
                min_price2 = price - max_profit1
            if price - min_price2 > max_profit2:
                max_profit2 = price - min_price2
        return max_profit2