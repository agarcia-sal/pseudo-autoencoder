class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # Quick check: if the sum of all numbers is less than desiredTotal, cannot win
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False

        # If desiredTotal is zero or negative, first player wins immediately
        if desiredTotal <= 0:
            return True

        memo = {}

        def can_win(current_total: int, used_numbers: int) -> bool:
            if (current_total, used_numbers) in memo:
                return memo[(current_total, used_numbers)]

            for number in range(1, maxChoosableInteger + 1):
                bit = 1 << (number - 1)
                if not (used_numbers & bit):
                    # If taking number reaches or exceeds desiredTotal, or opponent cannot win next turn
                    if current_total + number >= desiredTotal or not can_win(current_total + number, used_numbers | bit):
                        memo[(current_total, used_numbers)] = True
                        return True

            memo[(current_total, used_numbers)] = False
            return False

        return can_win(0, 0)