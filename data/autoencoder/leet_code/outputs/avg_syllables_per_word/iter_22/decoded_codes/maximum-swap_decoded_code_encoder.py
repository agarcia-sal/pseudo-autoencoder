class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {}
        for i, d in enumerate(digits):
            last[int(d)] = i
        for i, d in enumerate(digits):
            for digit_candidate in range(9, int(d), -1):
                if digit_candidate in last and last[digit_candidate] > i:
                    digits[i], digits[last[digit_candidate]] = digits[last[digit_candidate]], digits[i]
                    return int(''.join(digits))
        return num