MOD = 10**9 + 7

def count_non_decreasing_subsequences(num: str) -> int:
    n = len(num)
    memo = {}

    def dp(i, prev_len):
        if i == n:
            return 1
        if (i, prev_len) in memo:
            return memo[(i, prev_len)]
        cnt = 0
        for length in range(1, n - i + 1):
            if num[i] == '0':
                break
            cur = num[i:i+length]
            if prev_len == 0 or cur >= num[i - prev_len:i]:
                cnt = (cnt + dp(i + length, length)) % MOD
        memo[(i, prev_len)] = cnt
        return cnt

    return dp(0, 0)