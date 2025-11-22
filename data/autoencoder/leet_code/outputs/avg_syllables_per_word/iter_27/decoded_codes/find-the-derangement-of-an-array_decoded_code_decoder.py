class Solution:
    def findDerangement(self, n: int) -> int:
        MODULO = 10**9 + 7

        if n == 1:
            return 0
        if n == 2:
            return 1

        previous_twice = 1  # D(1)
        previous_once = 0   # D(2) initially set as 0, but updated in loop; will handle carefully

        # Actually, from the pseudocode logic, initial assignments:
        # previous_twice = 1 --> corresponds to D(1)
        # previous_once = 0 --> corresponds to D(2) = 1 in pseudocode? 
        # In pseudocode they return 1 directly for n=2, so loop starts at 3.
        # So must double check initialization for the loop starting at 3.
        # Given that for n=3, current_value = (3-1) * (previous_once + previous_twice) mod
        # previous_twice = 1 (D(1)), previous_once=0 (D(2)) conflicts with D(2)=1
        # So swap initialization to:
        # D(1) = 0 (no derangement), D(2)=1
        # But pseudocode sets previous_twice=1, previous_once=0, and returns 1 for n=2 directly.
        # Carefully following pseudocode:
        # previous_twice = 1
        # previous_once = 0
        # Loop i=3,..n:
        # current_value = (i-1) * (previous_once + previous_twice) % MODULO
        # previous_twice = previous_once
        # previous_once = current_value
        # return previous_once

        # That means previous_twice represents D(2) and previous_once D(1)
        # So swap:

        previous_twice = 0  # D(1)
        previous_once = 1   # D(2)

        for i in range(3, n + 1):
            current_value = (i - 1) * (previous_once + previous_twice) % MODULO
            previous_twice = previous_once
            previous_once = current_value

        return previous_once