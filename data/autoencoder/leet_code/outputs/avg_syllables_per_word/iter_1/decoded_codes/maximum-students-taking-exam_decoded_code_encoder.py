def max_students(seats):
    m, n = len(seats), len(seats[0])

    def count_bits(x):
        return bin(x).count('1')

    # broken[i]: bitmask of broken seats in row i
    broken = []
    for row in seats:
        mask = 0
        for j, seat in enumerate(row):
            if seat == '#':
                mask |= (1 << j)
        broken.append(mask)

    def is_valid(a):
        return (a & (a >> 1)) == 0

    dp = [{} for _ in range(m)]

    for arrangement in range(1 << n):
        if is_valid(arrangement) and (arrangement & broken[0]) == 0:
            dp[0][arrangement] = count_bits(arrangement)

    for i in range(1, m):
        for arrangement in range(1 << n):
            if is_valid(arrangement) and (arrangement & broken[i]) == 0:
                max_students = 0
                for prev in dp[i-1]:
                    if (arrangement & (prev >> 1)) == 0 and (arrangement & (prev << 1)) == 0:
                        max_students = max(max_students, dp[i-1][prev])
                dp[i][arrangement] = max_students + count_bits(arrangement)

    return max(dp[m-1].values()) if dp[m-1] else 0