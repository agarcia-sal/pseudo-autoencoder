from functools import lru_cache

def longest_increasing_path(arr, d):
    n = len(arr)

    def neighbors(i):
        res = []
        # Check left neighbors
        for step in range(1, d + 1):
            j = i - step
            if j < 0:
                break
            if arr[j] < arr[i]:
                res.append(j)
            else:
                break

        # Check right neighbors
        for step in range(1, d + 1):
            j = i + step
            if j >= n:
                break
            if arr[j] < arr[i]:
                res.append(j)
            else:
                break
        return res

    @lru_cache(None)
    def dp(i):
        nbrs = neighbors(i)
        if not nbrs:
            return 1
        return 1 + max(dp(j) for j in nbrs)

    return max(dp(i) for i in range(n))