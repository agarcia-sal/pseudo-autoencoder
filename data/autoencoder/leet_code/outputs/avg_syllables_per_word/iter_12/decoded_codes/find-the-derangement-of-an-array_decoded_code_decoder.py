class Solution:
    def findDerangement(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 1:
            return 0
        if n == 2:
            return 1

        prev2, prev1 = 1, 0  # D(1)=0 stored in prev1, D(2)=1 stored in prev2 reversed in init to match loop logic

        for i in range(3, n + 1):
            current = (i - 1) * (prev1 + prev2) % MOD
            prev2, prev1 = prev1, current

        return prev1