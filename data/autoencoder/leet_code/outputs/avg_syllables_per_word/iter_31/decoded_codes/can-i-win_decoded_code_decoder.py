from typing import Dict, Tuple

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # If the sum of all numbers is less than desiredTotal, no one can reach desiredTotal
        total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if total_sum < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True

        memo: Dict[Tuple[int, int], bool] = {}

        def can_win(current_total: int, used_numbers: int) -> bool:
            if (current_total, used_numbers) in memo:
                return memo[(current_total, used_numbers)]

            for number in range(1, maxChoosableInteger + 1):
                bit_mask = 1 << number
                if used_numbers & bit_mask == 0:
                    # If picking number reaches or exceeds desiredTotal
                    # or opponent cannot win after picking number
                    if current_total + number >= desiredTotal or not can_win(current_total + number, used_numbers | bit_mask):
                        memo[(current_total, used_numbers)] = True
                        return True

            memo[(current_total, used_numbers)] = False
            return False

        return can_win(0, 0)