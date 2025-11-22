def largestNumber(cost, target):
    cost_to_digit = {c: str(i+1) for i, c in enumerate(cost)}
    dp = [""] + ["-1"] * target
    for t in range(1, target+1):
        for c, d in cost_to_digit.items():
            if t >= c and dp[t - c] != "-1":
                cand = d + dp[t - c]
                if dp[t] == "-1" or len(cand) > len(dp[t]) or (len(cand) == len(dp[t]) and cand > dp[t]):
                    dp[t] = cand
    return dp[target] if dp[target] != "-1" else "0"