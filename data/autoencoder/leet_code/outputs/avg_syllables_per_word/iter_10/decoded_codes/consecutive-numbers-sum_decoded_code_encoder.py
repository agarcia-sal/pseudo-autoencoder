class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        two_n = 2 * n
        k = 1
        while k * (k + 1) <= two_n:
            if two_n % k == 0:
                m = (two_n // k - k + 1) / 2
                if m > 0 and m.is_integer():
                    count += 1
            k += 1
        return count