from bisect import bisect_right

def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    end_times = [end for _, end, _ in jobs]
    dp = [0] * (len(jobs) + 1)

    for i in range(1, len(jobs) + 1):
        start, end, p = jobs[i-1]
        j = bisect_right(end_times, start)
        dp[i] = max(dp[i-1], dp[j] + p)

    return dp[-1]