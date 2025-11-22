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
            for i, ch in enumerate(s):
                start = 0
                if i == 0:
                    start = 1
                for d in range(start, int(ch)):
                    if d not in seen:
                        count += self.perm(9 - i, length - i - 1)
                if int(ch) in seen:
                    break
                seen.add(int(ch))
            else:
                count += 1
            return count

        return n - count_unique_digits(n)