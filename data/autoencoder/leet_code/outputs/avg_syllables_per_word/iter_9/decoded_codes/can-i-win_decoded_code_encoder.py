class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True

        memo = {}

        def can_win(current_total, used_numbers):
            if (current_total, used_numbers) in memo:
                return memo[(current_total, used_numbers)]

            for number in range(1, maxChoosableInteger + 1):
                bit = 1 << (number - 1)
                if not used_numbers & bit:
                    if current_total + number >= desiredTotal or not can_win(current_total + number, used_numbers | bit):
                        memo[(current_total, used_numbers)] = True
                        return True

            memo[(current_total, used_numbers)] = False
            return False

        return can_win(0, 0)