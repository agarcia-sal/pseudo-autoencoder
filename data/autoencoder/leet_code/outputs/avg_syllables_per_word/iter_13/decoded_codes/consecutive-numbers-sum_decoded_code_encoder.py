class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        two_n = 2 * n
        for k in range(1, n + 1):
            if two_n % k == 0:
                m = (two_n // k - k + 1) / 2
                if m > 0 and m == int(m):
                    count += 1
        return count