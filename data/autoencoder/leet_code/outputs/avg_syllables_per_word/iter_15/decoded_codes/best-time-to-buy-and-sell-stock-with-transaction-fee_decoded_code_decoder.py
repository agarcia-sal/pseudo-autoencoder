from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = float('-inf')
        for price in prices:
            possible_cash_profit = hold + price - fee
            if possible_cash_profit > cash:
                cash = possible_cash_profit
            possible_hold_profit = cash - price
            if possible_hold_profit > hold:
                hold = possible_hold_profit
        return cash