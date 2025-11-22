from typing import List
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price1 = math.inf
        min_price2 = math.inf
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