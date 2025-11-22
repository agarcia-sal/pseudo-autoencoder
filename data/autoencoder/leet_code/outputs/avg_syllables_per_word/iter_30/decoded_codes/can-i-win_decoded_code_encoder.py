class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True

        memo = {}

        def can_win(current_total: int, used_numbers: int) -> bool:
            key = (current_total, used_numbers)
            if key in memo:
                return memo[key]
            for number in range(1, maxChoosableInteger + 1):
                bit = 1 << number
                if (used_numbers & bit) == 0:
                    if current_total + number >= desiredTotal or not can_win(current_total + number, used_numbers | bit):
                        memo[key] = True
                        return True
            memo[key] = False
            return False

        return can_win(0, 0)