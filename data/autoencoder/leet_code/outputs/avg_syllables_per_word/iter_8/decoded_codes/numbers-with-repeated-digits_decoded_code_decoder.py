class Solution:
    def numDupDigitsAtMostN(self, n):
        def count_unique_digits(x):
            s = str(x)
            length = len(s)
            count = 0
            for i in range(1, length):
                count += 9 * self.perm(9, i - 1)
            seen = set()
            for i, ch in enumerate(s):
                digit = int(ch)
                start = 1 if i == 0 else 0
                for d in range(start, digit):
                    if d not in seen:
                        count += self.perm(9 - i, length - i - 1)
                if digit in seen:
                    break
                seen.add(digit)
            else:
                count += 1
            return count

        return n - count_unique_digits(n)

    def perm(self, m, n):
        if n == 0:
            return 1
        result = 1
        for i in range(n):
            result *= m - i
        return result