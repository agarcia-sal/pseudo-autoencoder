def compute_result(nums):
    MOD = 10**9 + 7
    max_num = max(nums)
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    prefix_sum = [0] * (max_num + 1)
    for num in count:
        prefix_sum[num] += count[num]
    for i in range(1, max_num + 1):
        prefix_sum[i] += prefix_sum[i - 1]

    result = 0
    for num in count:
        for k in range(1, max_num // num + 1):
            start = num * k
            end = min(num * (k + 1) - 1, max_num)
            c = prefix_sum[end] - (prefix_sum[start - 1] if start > 0 else 0)
            result = (result + c * k * count[num]) % MOD

    return result