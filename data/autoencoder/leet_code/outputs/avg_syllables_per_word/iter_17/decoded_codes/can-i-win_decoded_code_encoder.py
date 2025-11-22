class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # Quick check: if sum of all numbers is less than desiredTotal, can't win
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
                # Check if number is unused (bit not set)
                if (used_numbers & (1 << number)) == 0:
                    next_total = current_total + number
                    next_used = used_numbers | (1 << number)
                    if next_total >= desiredTotal or not can_win(next_total, next_used):
                        memo[key] = True
                        return True

            memo[key] = False
            return False

        return can_win(0, 0)