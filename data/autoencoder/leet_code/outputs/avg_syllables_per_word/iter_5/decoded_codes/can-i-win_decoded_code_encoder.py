class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True

        memo = {}

        def can_win(current_total, used_numbers):
            if used_numbers in memo:
                return memo[used_numbers]
            for number in range(1, maxChoosableInteger + 1):
                mask = 1 << (number - 1)
                if not used_numbers & mask:
                    if current_total + number >= desiredTotal or not can_win(current_total + number, used_numbers | mask):
                        memo[used_numbers] = True
                        return True
            memo[used_numbers] = False
            return False

        return can_win(0, 0)