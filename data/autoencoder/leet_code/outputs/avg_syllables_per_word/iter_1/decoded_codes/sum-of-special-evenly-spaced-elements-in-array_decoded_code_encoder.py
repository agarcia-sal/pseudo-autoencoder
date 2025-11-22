def solve(nums, queries):
    MOD = 10**9 + 7
    n = len(nums)
    max_y = max(y for _, y in queries)

    prefix_sums = [[0] * n for _ in range(max_y + 1)]

    for y in range(1, max_y + 1):
        for i in range(n - 1, -1, -1):
            prefix_sums[y][i] = nums[i]
            if i + y < n:
                prefix_sums[y][i] += prefix_sums[y][i + y]

    answer = []
    for x, y in queries:
        answer.append(prefix_sums[y][x] % MOD)

    return answer