class Solution:
    def maxProfit(self, prices, fee):
        cash = 0
        hold = float('-inf')

        for price in prices:
            potential_cash_after_selling = hold + price - fee
            cash = max(cash, potential_cash_after_selling)
            potential_hold_after_buying = cash - price
            hold = max(hold, potential_hold_after_buying)

        return cash