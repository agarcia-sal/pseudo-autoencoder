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
                digit_value = int(digit)
                start_range = 1 if i == 0 else 0
                for d in range(start_range, digit_value):
                    if d not in seen:
                        count += perm(9 - i, length - i - 1)
                if digit_value in seen:
                    break
                seen.add(digit_value)
            else:
                count += 1
            return count

        unique_count = count_unique_digits(n)
        return n - unique_count