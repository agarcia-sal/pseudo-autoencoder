class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}
        for i, d in enumerate(digits):
            digit = int(d)
            for d2 in range(9, digit, -1):
                if d2 in last and last[d2] > i:
                    digits[i], digits[last[d2]] = digits[last[d2]], digits[i]
                    return int("".join(digits))
        return num