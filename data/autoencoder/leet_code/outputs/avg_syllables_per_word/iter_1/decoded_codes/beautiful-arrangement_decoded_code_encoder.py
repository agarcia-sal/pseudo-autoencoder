def countArrangement(n):
    def backtrack(used, i):
        if i > n:
            return 1
        c = 0
        for x in range(1, n + 1):
            if not used[x] and (x % i == 0 or i % x == 0):
                used[x] = True
                c += backtrack(used, i + 1)
                used[x] = False
        return c

    used = [False] * (n + 1)
    return backtrack(used, 1)