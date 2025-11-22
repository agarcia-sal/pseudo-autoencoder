from math import inf

class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if not prices or k == 0:
            return 0

        n = len(prices)

        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        def initialize_hold_and_release_arrays(limit: int):
            hold_array = [-inf] * (limit + 1)
            release_array = [0] * (limit + 1)
            return hold_array, release_array

        hold, release = initialize_hold_and_release_arrays(k)

        for price in prices:
            for transaction_index in range(1, k + 1):
                hold[transaction_index] = max(hold[transaction_index], release[transaction_index - 1] - price)
                release[transaction_index] = max(release[transaction_index], hold[transaction_index] + price)

        return release[k]