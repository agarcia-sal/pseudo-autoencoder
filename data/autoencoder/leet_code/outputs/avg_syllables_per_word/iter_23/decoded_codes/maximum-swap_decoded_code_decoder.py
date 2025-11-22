class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {}
        for i, d in enumerate(digits):
            last[int(d)] = i

        for i, d in enumerate(digits):
            digit_value = int(d)
            for candidate_digit in range(9, digit_value, -1):
                if candidate_digit in last and last[candidate_digit] > i:
                    pos = last[candidate_digit]
                    digits[i], digits[pos] = digits[pos], digits[i]
                    return int("".join(digits))
        return num