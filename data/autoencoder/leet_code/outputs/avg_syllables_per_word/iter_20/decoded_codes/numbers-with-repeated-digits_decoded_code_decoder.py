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
            # Count numbers with unique digits and length less than that of x
            for i in range(1, length):
                count += 9 * perm(9, i - 1)

            seen = set()
            for i, digit_char in enumerate(s):
                digit = int(digit_char)
                start_d = 1 if i == 0 else 0
                for d in range(start_d, digit):
                    if d not in seen:
                        count += perm(9 - i, length - i - 1)
                if digit in seen:
                    break
                seen.add(digit)
            else:
                # Completed loop without break means x itself has unique digits
                count += 1
            return count

        return n - count_unique_digits(n)