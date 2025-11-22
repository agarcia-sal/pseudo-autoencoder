from typing import Dict, Tuple

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # If the sum of all numbers is less than desiredTotal, can't win
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False
        # If desiredTotal is zero or less, first player trivially wins
        if desiredTotal <= 0:
            return True

        memo: Dict[Tuple[int, int], bool] = {}

        def can_win(current_total: int, used_numbers: int) -> bool:
            key = (current_total, used_numbers)
            if key in memo:
                return memo[key]

            for number in range(1, maxChoosableInteger + 1):
                mask = 1 << number
                if used_numbers & mask == 0:
                    next_total = current_total + number
                    if next_total >= desiredTotal or not can_win(next_total, used_numbers | mask):
                        memo[key] = True
                        return True
            memo[key] = False
            return False

        return can_win(0, 0)