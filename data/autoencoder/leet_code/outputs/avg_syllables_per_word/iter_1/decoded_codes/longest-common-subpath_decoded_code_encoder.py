def longest_common_subpath(paths):
    INF = float('inf')

    def hash_subpaths(path, L):
        P, MOD = 113, 10**9 + 7
        h, p = 0, 1
        for i in range(L):
            h = (h * P + path[i]) % MOD
            p = (p * P) % MOD
        hs = {h}
        for i in range(L, len(path)):
            h = (h * P + path[i] - path[i - L] * p) % MOD
            hs.add(h)
        return hs

    def check_common_subpath(L):
        if L == 0:
            return True
        common = hash_subpaths(paths[0], L)
        for path in paths[1:]:
            common &= hash_subpaths(path, L)
            if not common:
                return False
        return bool(common)

    left, right = 0, min(len(p) for p in paths)
    while left < right:
        mid = (left + right + 1) // 2
        if check_common_subpath(mid):
            left = mid
        else:
            right = mid - 1

    return left