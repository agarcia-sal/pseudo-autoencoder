class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {}
        for i, d in enumerate(digits):
            last[int(d)] = i
        for i, d in enumerate(digits):
            for candidate in range(9, int(d), -1):
                if candidate in last and last[candidate] > i:
                    j = last[candidate]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))
        return num