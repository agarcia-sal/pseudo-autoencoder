class Solution:
    def largestNumber(self, cost, target):
        not_possible = "#"
        # Map cost value to digit as string, e.g. cost[0] -> '1'
        cost_to_digit = {c: str(i + 1) for i, c in enumerate(cost)}

        # dp[t] holds the largest number (as string) to reach cost t or '#' if impossible
        dp = [""] + [not_possible] * target

        for t in range(1, target + 1):
            for c, d in cost_to_digit.items():
                if t >= c and dp[t - c] != not_possible:
                    candidate = d + dp[t - c]  # prepend digit for lex max sorting by length then lex

                    # Update dp[t] if candidate is better:
                    # Longer length preferred, if same length lex greater preferred
                    if dp[t] == not_possible or len(candidate) > len(dp[t]) or (len(candidate) == len(dp[t]) and candidate > dp[t]):
                        dp[t] = candidate

        # dp[target] is the candidate reversed (digits put front first), so reverse before returning.
        # However, the pseudocode builds candidate as d + dp[t - c], 
        # so the digits prepend, earliest digit in front, which means the number is reversed, to correct,
        # reverse string before returning.

        return dp[target][::-1] if dp[target] != not_possible else "0"