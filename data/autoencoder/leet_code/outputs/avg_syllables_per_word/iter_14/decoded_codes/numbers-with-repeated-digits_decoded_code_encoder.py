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
            for i, digit_char in enumerate(s):
                start_range = 0
                if i == 0:
                    start_range = 1
                digit_value = int(digit_char)
                for d in range(start_range, digit_value):
                    if d not in seen:
                        count += perm(9 - i, length - i - 1)
                if digit_value in seen:
                    break
                seen.add(digit_value)
            else:
                count += 1
            return count

        total_unique_digit_numbers = count_unique_digits(n)
        result = n - total_unique_digit_numbers
        return result