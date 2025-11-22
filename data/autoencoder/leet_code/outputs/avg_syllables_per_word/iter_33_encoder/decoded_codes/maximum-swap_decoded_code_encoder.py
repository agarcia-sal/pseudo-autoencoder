class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {}
        for i, d in enumerate(digits):
            last[int(d)] = i
        for i, d in enumerate(digits):
            current_digit = int(d)
            for d2 in range(9, current_digit, -1):
                if d2 in last and last[d2] > i:
                    swap_position = last[d2]
                    digits[i], digits[swap_position] = digits[swap_position], digits[i]
                    return int("".join(digits))
        return num