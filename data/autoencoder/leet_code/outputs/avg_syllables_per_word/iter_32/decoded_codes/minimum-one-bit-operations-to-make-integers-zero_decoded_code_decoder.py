class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0

        k = 0
        while (1 << (k + 1)) <= n:
            k += 1

        most_significant_bit = 1 << k
        return ((1 << (k + 1)) - 1) - self.minimumOneBitOperations(n ^ most_significant_bit)