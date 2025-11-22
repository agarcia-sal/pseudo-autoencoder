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
            # Count numbers with unique digits of length less than 'length'
            for i in range(1, length):
                # 9 choices for the first digit (no leading zero),
                # then perm(9, i - 1) for the remaining digits
                count += 9 * perm(9, i - 1)

            seen = set()
            for i, ch in enumerate(s):
                digit = int(ch)
                # For each digit smaller than current digit, try digits that haven't been used before
                # and respect leading digit constraints (no leading zero)
                start_digit = 1 if i == 0 else 0
                for d in range(start_digit, digit):
                    if d not in seen:
                        count += perm(9 - i, length - i - 1)
                if digit in seen:
                    # Duplicate digit found, break
                    break
                seen.add(digit)
            else:
                # No break means number itself has unique digits, count it
                count += 1
            return count

        return n - count_unique_digits(n)