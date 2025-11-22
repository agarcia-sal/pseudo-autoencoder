from typing import Set

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        def count_unique_digits(x: int) -> int:
            s = str(x)
            length = len(s)
            count = 0
            for i in range(1, length):
                count += 9 * self.perm(9, i - 1)
            seen: Set[int] = set()
            for i, digit in enumerate(s):
                digit_int = int(digit)
                start = 1 if i == 0 else 0
                for d in range(start, digit_int):
                    if d not in seen:
                        count += self.perm(9 - i, length - i - 1)
                if digit_int in seen:
                    break
                seen.add(digit_int)
            else:
                count += 1
            return count

        return n - count_unique_digits(n)

    def perm(self, m: int, n: int) -> int:
        if n == 0:
            return 1
        result = 1
        for i in range(n):
            result *= m - i
        return result