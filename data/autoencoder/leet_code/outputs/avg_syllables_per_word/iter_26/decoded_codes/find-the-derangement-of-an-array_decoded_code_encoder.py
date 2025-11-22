class Solution:
    def findDerangement(self, n: int) -> int:
        MODULO = 10**9 + 7

        if n == 1:
            return 0
        if n == 2:
            return 1

        previous_previous_value = 1
        previous_value = 0

        for index in range(3, n + 1):
            current_value = (index - 1) * (previous_value + previous_previous_value) % MODULO
            previous_previous_value = previous_value
            previous_value = current_value

        return previous_value