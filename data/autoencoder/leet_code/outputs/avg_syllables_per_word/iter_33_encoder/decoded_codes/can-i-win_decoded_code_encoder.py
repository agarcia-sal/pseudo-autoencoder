class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # If the sum of all choosable numbers is less than desiredTotal, no way to win
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False
        # If desiredTotal is zero or less, first player wins by default
        if desiredTotal <= 0:
            return True

        memo = {}

        def can_win(current_total: int, used_numbers: int) -> bool:
            if (current_total, used_numbers) in memo:
                return memo[(current_total, used_numbers)]
            for number in range(1, maxChoosableInteger + 1):
                bit = 1 << (number - 1)
                if used_numbers & bit == 0:
                    if current_total + number >= desiredTotal or not can_win(current_total + number, used_numbers | bit):
                        memo[(current_total, used_numbers)] = True
                        return True
            memo[(current_total, used_numbers)] = False
            return False

        return can_win(0, 0)