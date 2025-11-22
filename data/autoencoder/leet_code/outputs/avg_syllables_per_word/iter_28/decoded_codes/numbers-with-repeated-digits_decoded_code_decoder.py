from typing import Set


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        def perm(m: int, n: int) -> int:
            if n == 0:
                return 1
            result = 1
            for i in range(n):
                result *= m - i
            return result

        def count_unique_digits(x: int) -> int:
            s = str(x)
            length = len(s)
            count = 0
            for i in range(1, length):
                count += 9 * perm(9, i - 1)
            seen: Set[int] = set()
            for i in range(length):
                digit = int(s[i])
                start_range = 1 if i == 0 else 0
                for d in range(start_range, digit):
                    if d not in seen:
                        count += perm(9 - i, length - i - 1)
                if digit in seen:
                    break
                seen.add(digit)
            else:
                count += 1
            return count

        unique_count = count_unique_digits(n)
        return n - unique_count