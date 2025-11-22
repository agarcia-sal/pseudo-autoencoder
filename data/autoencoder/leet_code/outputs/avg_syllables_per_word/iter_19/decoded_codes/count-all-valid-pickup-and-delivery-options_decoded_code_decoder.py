class Solution:
    def countOrders(self, n):
        MOD = 10**9 + 7
        count = 1
        for i in range(2, n + 1):
            count = count * i * 2 * i - 1
            count %= MOD
        return count