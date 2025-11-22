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

            seen = set()
            for i, digit in enumerate(s):
                d = int(digit)
                start = 1 if i == 0 else 0
                for x_digit in range(start, d):
                    if x_digit not in seen:
                        count += perm(9 - i, length - i - 1)
                if d in seen:
                    break
                seen.add(d)
            else:
                count += 1
            return count

        return n - count_unique_digits(n)