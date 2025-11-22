from typing import List, Dict

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # Map each cost to the digit (as string) it can represent (digits 1 through 9)
        cost_to_digit: Dict[int, str] = {}
        for i, c in enumerate(cost):
            # For duplicate costs, keep the digit with the highest value for tie-breaking later
            d = str(i + 1)
            if c not in cost_to_digit or d > cost_to_digit[c]:
                cost_to_digit[c] = d

        # dp[t] will store the best number (string) we can form with cost exactly t
        # Initialize dp array with sentinel "-1" (impossible states), dp[0] = "" (empty number)
        dp = ["-1"] * (target + 1)
        dp[0] = ""

        for t in range(1, target + 1):
            for c, d in cost_to_digit.items():
                if t >= c and dp[t - c] != "-1":
                    candidate = d + dp[t - c]
                    current = dp[t]
                    # Update dp[t] if:
                    # 1) current is "-1" (no solution yet for t)
                    # 2) length of candidate is greater (longer number preferred)
                    # 3) length equal but candidate lex order is greater (numerically larger)
                    if (current == "-1" or
                        len(candidate) > len(current) or
                        (len(candidate) == len(current) and candidate > current)):
                        dp[t] = candidate

        return dp[target] if dp[target] != "-1" else "0"