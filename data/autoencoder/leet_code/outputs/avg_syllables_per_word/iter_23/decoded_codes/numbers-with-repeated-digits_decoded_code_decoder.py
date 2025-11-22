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
            # Count unique-digit numbers with length less than length of x
            for i in range(1, length):
                count += 9 * perm(9, i - 1)

            seen = set()
            for i, ch in enumerate(s):
                digit = int(ch)
                start = 0 if i == 0 else 1
                for d in range(start, digit):
                    if d not in seen:
                        count += perm(9 - i, length - i - 1)
                if digit in seen:
                    break
                seen.add(digit)
            else:
                # Completed for loop without break means no duplicate digits in x itself
                count += 1
            return count

        return n - count_unique_digits(n)