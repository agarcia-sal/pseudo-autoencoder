class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}

        for i, d_char in enumerate(digits):
            d = int(d_char)
            for d2 in range(9, d, -1):
                if last.get(d2, -1) > i:
                    j = last[d2]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))
        return num