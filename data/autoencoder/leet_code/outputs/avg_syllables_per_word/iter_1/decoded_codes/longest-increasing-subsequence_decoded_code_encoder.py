from bisect import bisect_left

def lengthOfLIS(nums):
    if not nums:
        return 0
    dp = []
    for num in nums:
        i = bisect_left(dp, num)
        if i == len(dp):
            dp.append(num)
        else:
            dp[i] = num
    return len(dp)