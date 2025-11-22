class Solution:
    def maximumSwap(self, num):
        digits = list(str(num))
        last = {int(x): i for i, x in enumerate(digits)}
        for i, d in enumerate(digits):
            digit = int(d)
            for d2 in range(9, digit, -1):
                if last.get(d2, -1) > i:
                    j = last[d2]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))
        return num