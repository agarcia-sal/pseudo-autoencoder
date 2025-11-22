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

            # Count numbers with unique digits and length less than length of x
            for i in range(1, length):
                count += 9 * perm(9, i - 1)

            seen = set()
            position = 0
            while position < length:
                current_digit = int(s[position])
                for d in range(current_digit):
                    if position == 0 and d == 0:
                        continue
                    if d not in seen:
                        count += perm(9 - position, length - position - 1)
                if current_digit in seen:
                    break
                seen.add(current_digit)
                position += 1

            if position == length:
                count += 1

            return count

        return n - count_unique_digits(n)