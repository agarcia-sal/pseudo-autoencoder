class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True
        memo = {}

        def can_win(current_total, used_numbers):
            key = (current_total, used_numbers)
            if key in memo:
                return memo[key]
            for number in range(1, maxChoosableInteger + 1):
                mask = 1 << number
                if used_numbers & mask == 0:
                    if current_total + number >= desiredTotal or not can_win(current_total + number, used_numbers | mask):
                        memo[key] = True
                        return True
            memo[key] = False
            return False

        return can_win(0, 0)