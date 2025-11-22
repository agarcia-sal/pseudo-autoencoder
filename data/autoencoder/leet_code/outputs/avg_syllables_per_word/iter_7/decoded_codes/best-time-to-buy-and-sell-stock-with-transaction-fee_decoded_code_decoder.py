from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = float('-inf')

        for price in prices:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)

        return cash