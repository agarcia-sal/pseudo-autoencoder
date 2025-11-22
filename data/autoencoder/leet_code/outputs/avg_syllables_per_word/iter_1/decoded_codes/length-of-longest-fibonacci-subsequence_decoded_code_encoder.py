def len_longest_fib_subseq(arr):
    idx = {v: i for i, v in enumerate(arr)}
    dp = {}
    max_len = 0
    n = len(arr)
    for k in range(n):
        for j in range(k):
            i = idx.get(arr[k] - arr[j], -1)
            if i >= 0 and i < j:
                dp[j, k] = dp.get((i, j), 2) + 1
                max_len = max(max_len, dp[j, k])
    return max_len if max_len >= 3 else 0