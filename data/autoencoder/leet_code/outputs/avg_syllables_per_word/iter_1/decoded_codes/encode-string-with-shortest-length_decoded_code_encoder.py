def encode(s):
    def dp(i, j):
        sub = s[i:j+1]
        n = j - i + 1
        if n < 5:
            return sub

        shortest = sub
        for k in range(1, n // 2 + 1):
            if n % k == 0 and sub == sub[:k] * (n // k):
                cand = str(n // k) + "[" + dp(i, i + k - 1) + "]"
                if len(cand) < len(shortest):
                    shortest = cand

        for k in range(i, j):
            combined = dp(i, k) + dp(k + 1, j)
            if len(combined) < len(shortest):
                shortest = combined

        return shortest

    return dp(0, len(s) - 1)