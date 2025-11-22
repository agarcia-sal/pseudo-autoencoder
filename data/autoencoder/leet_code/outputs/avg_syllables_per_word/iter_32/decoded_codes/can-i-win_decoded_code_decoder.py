from typing import Dict, Tuple

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # If the sum of all numbers from 1 to maxChoosableInteger is less than desiredTotal, player 1 cannot win
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False

        # If desiredTotal is less than or equal to zero, player 1 wins by default
        if desiredTotal <= 0:
            return True

        memo: Dict[Tuple[int, int], bool] = {}

        def can_win(current_total: int, used_numbers: int) -> bool:
            key = (current_total, used_numbers)
            if key in memo:
                return memo[key]

            for number in range(1, maxChoosableInteger + 1):
                bit_mask = 1 << number
                # If the number has not been used yet
                if (used_numbers & bit_mask) == 0:
                    # If picking this number reaches or exceeds desiredTotal, or opponent cannot win next turn
                    if current_total + number >= desiredTotal or not can_win(current_total + number, used_numbers | bit_mask):
                        memo[key] = True
                        return True

            memo[key] = False
            return False

        return can_win(0, 0)