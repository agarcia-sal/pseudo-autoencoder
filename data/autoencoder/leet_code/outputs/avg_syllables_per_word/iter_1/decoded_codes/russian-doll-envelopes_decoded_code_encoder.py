from bisect import bisect_left

def max_envelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    for _, h in envelopes:
        i = bisect_left(dp, h)
        if i == len(dp):
            dp.append(h)
        else:
            dp[i] = h
    return len(dp)