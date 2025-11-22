from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0:
            return 0
        min_price1 = float('inf')
        min_price2 = float('inf')
        max_profit1 = 0
        max_profit2 = 0
        for price in prices:
            if min_price1 > price:
                min_price1 = price
            if max_profit1 < price - min_price1:
                max_profit1 = price - min_price1
            if min_price2 > price - max_profit1:
                min_price2 = price - max_profit1
            if max_profit2 < price - min_price2:
                max_profit2 = price - min_price2
        return max_profit2