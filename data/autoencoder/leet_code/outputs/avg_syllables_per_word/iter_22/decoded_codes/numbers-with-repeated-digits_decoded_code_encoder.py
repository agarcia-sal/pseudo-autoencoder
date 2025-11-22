class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        def count_unique_digits(x: int) -> int:
            s = str(x)
            length = len(s)
            count = 0

            # Count numbers with unique digits of length less than length of x
            for i in range(1, length):
                count += 9 * self.perm(9, i - 1)

            seen = set()
            for i, digit_char in enumerate(s):
                digit = int(digit_char)
                # d ranges from 0 (if i > 0) else 1 (because no leading zero) to digit-1
                start = 0 if i > 0 else 1
                for d in range(start, digit):
                    if d not in seen:
                        count += self.perm(9 - i, length - i - 1)
                if digit in seen:
                    break
                seen.add(digit)
            else:
                # No break occurred, all digits unique
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