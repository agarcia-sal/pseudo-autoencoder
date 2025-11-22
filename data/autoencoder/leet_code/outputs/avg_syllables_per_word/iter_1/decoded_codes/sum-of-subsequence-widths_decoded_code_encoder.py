MOD = 10**9 + 7

nums.sort()
n = len(nums)
power = [1] * n
for i in range(1, n):
    power[i] = (power[i-1] * 2) % MOD

total = 0
for i in range(n):
    total += nums[i] * (power[i] - power[n - i - 1]) 
    total %= MOD

return total