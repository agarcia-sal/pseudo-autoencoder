class Solution:
    def findDerangement(self, n: int) -> int:
        MODULO = 10**9 + 7

        if n == 1:
            return 0
        if n == 2:
            return 1

        previous_two = 1  # D(1)
        previous_one = 0  # D(2)

        for index in range(3, n + 1):
            current_value = (index - 1) * (previous_one + previous_two) % MODULO
            previous_two, previous_one = previous_one, current_value

        return previous_one