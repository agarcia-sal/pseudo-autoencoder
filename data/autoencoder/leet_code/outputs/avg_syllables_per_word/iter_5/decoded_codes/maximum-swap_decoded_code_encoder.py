class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}

        for i, d in enumerate(digits):
            for d2 in range(9, int(d), -1):
                if d2 in last and last[d2] > i:
                    j = last[d2]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))

        return num