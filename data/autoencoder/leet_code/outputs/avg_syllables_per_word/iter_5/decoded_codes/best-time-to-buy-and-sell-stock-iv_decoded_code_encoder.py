class Solution:
    def maxProfit(self, k, prices):
        if not prices or k == 0:
            return 0

        n = len(prices)
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        hold = [float('-inf')] * (k + 1)
        release = [0] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                hold[i] = max(hold[i], release[i - 1] - price)
                release[i] = max(release[i], hold[i] + price)

        return release[k]