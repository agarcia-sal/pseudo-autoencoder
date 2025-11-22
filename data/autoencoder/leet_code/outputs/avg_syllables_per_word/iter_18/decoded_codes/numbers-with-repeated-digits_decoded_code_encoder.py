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
            # Count numbers with unique digits that have fewer digits than length
            count = 0
            for i in range(1, length):
                count += 9 * perm(9, i - 1)

            seen = set()
            for i, ch in enumerate(s):
                digit = int(ch)
                start = 1 if i == 0 else 0
                for d in range(start, digit):
                    if d not in seen:
                        count += perm(9 - i, length - i - 1)
                if digit in seen:
                    break
                seen.add(digit)
            else:
                count += 1  # Count the number itself if all digits unique
            return count

        total = n
        unique = count_unique_digits(n)
        return total - unique