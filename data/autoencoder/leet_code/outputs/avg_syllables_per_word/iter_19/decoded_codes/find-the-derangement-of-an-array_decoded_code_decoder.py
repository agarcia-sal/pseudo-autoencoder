class Solution:
    def findDerangement(self, n):
        MOD = 10**9 + 7

        if n == 1:
            return 0
        if n == 2:
            return 1

        prev2 = 1
        prev1 = 0

        for i in range(3, n + 1):
            sum_of_previous_two = prev1 + prev2
            product = (i - 1) * sum_of_previous_two
            current = product % MOD
            prev2 = prev1
            prev1 = current

        return prev1