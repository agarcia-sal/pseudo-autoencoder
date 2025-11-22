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

        hold = initializeHoldArray(k)
        release = initializeReleaseArray(k)

        for price in prices:
            for j in range(1, k + 1):
                hold[j] = max(hold[j], release[j - 1] - price)
                release[j] = max(release[j], hold[j] + price)

        return release[k]


def initializeHoldArray(k: int) -> list[int]:
    # Initialize hold array with -infinity for indices 1 to k, zero at index 0 for convenience
    # Using float('-inf') represents that we haven't bought any stock yet for those transactions
    return [0] + [float('-inf')] * k


def initializeReleaseArray(k: int) -> list[int]:
    # Initialize release array with zeros; release[0] = 0 as no transaction done
    return [0] * (k + 1)