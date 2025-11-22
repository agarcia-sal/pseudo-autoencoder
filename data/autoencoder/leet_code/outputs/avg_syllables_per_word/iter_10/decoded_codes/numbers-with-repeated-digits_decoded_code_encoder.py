class Solution:
    def perm(self, m: int, n: int) -> int:
        if n == 0:
            return 1
        result = 1
        for i in range(n):
            result *= m - i
        return result

    def numDupDigitsAtMostN(self, n: int) -> int:
        def count_unique_digits(x: int) -> int:
            s = str(x)
            length = len(s)
            count = 0
            for i in range(1, length):
                count += 9 * self.perm(9, i - 1)
            seen = set()
            for i in range(length):
                digit = int(s[i])
                for d in range(0 if i else 1, digit):
                    if d not in seen:
                        count += self.perm(9 - i, length - i - 1)
                if digit in seen:
                    break
                seen.add(digit)
            else:
                count += 1
            return count

        unique_count = count_unique_digits(n)
        return n - unique_count