class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        count = 10
        available_digits = 9
        choices = 9
        for i in range(2, n + 1):
            choices *= available_digits
            count += choices
            available_digits -= 1
            if available_digits == 0:  # No digits left to choose; break early
                break
        return count