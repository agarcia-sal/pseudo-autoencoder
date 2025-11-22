def find_integers(n: int) -> int:
    b = bin(n)[2:]
    L = len(b)

    dp = [0] * (L + 1)
    dp[0] = 1
    dp[1] = 2
    for i in range(2, L + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    res = 0
    prev = 0
    for i in range(L):
        if b[i] == '1':
            res += dp[L - i - 1]
            if prev == 1:
                res -= 1
                break
            prev = 1
        else:
            prev = 0

    return res + 1