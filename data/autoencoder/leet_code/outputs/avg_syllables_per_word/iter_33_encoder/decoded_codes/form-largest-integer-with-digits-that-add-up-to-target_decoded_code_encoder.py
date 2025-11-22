from typing import List

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # Map each cost value to its corresponding digit as a string (1-based index)
        cost_to_digit = {c: str(i + 1) for i, c in enumerate(cost)}

        # dp[t] stores the largest number string that can be formed with total cost t
        dp = ['-1'] * (target + 1)
        dp[0] = ''

        for t in range(1, target + 1):
            for c, d in cost_to_digit.items():
                if t >= c and dp[t - c] != '-1':
                    candidate = d + dp[t - c]
                    current = dp[t]
                    # Update dp[t] if it's -1 or candidate is better by length or lex order
                    if (current == '-1' 
                        or len(candidate) > len(current) 
                        or (len(candidate) == len(current) and candidate > current)):
                        dp[t] = candidate

        return dp[target] if dp[target] != '-1' else '0'