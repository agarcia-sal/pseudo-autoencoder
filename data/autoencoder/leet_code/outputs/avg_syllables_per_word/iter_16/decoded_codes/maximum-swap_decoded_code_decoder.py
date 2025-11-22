class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}
        for i, d in enumerate(digits):
            for d2 in range(9, int(d), -1):
                pos = last.get(d2, -1)
                if pos > i:
                    digits[i], digits[pos] = digits[pos], digits[i]
                    return int("".join(digits))
        return num