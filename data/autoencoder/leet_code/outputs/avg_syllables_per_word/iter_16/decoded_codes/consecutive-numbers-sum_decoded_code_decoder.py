class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        for k in range(1, n + 1):
            if (2 * n) % k == 0:
                numerator = (2 * n) // k - (k - 1)
                if numerator > 0 and numerator % 2 == 0:
                    count += 1
        return count