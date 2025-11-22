class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True

        memo = {}

        def can_win(current_total: int, used_numbers: int) -> bool:
            if (current_total, used_numbers) in memo:
                return memo[(current_total, used_numbers)]
            for num in range(1, maxChoosableInteger + 1):
                bit = 1 << num
                if (used_numbers & bit) == 0:
                    if current_total + num >= desiredTotal or not can_win(current_total + num, used_numbers | bit):
                        memo[(current_total, used_numbers)] = True
                        return True
            memo[(current_total, used_numbers)] = False
            return False

        return can_win(0, 0)