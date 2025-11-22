class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {}
        for i, d in enumerate(digits):
            last[int(d)] = i
        for i, d in enumerate(digits):
            current_digit = int(d)
            for digit_candidate in range(9, current_digit, -1):
                if digit_candidate in last and last[digit_candidate] > i:
                    j = last[digit_candidate]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int(''.join(digits))
        return num