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
            for digit_count in range(1, length):
                count += 9 * perm(9, digit_count - 1)

            seen_digits = set()
            for i in range(length):
                digit_value = int(s[i])
                for candidate_digit in range(0 if i == 0 else 0, digit_value):
                    if candidate_digit not in seen_digits:
                        count += perm(9 - i, length - i - 1)
                if digit_value in seen_digits:
                    break
                seen_digits.add(digit_value)
            else:
                count += 1

            return count

        return n - count_unique_digits(n)