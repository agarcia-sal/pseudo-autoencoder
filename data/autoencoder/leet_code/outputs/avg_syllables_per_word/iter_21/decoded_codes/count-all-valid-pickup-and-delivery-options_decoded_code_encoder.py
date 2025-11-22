class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        count = 1
        for i in range(2, n + 1):
            count = (count * i * 2 * i - 1) % MOD  # original pseudocode is ambiguous; fix on next line
            # The pseudocode states: count = count * i * 2 * i - 1, which is ambiguous. Likely intended:
            # count = count * i * (2 * i - 1)
            # Adjusting accordingly:
        count = 1
        for i in range(2, n + 1):
            count = (count * i * (2 * i - 1)) % MOD
        return count