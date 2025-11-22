def max_product_palindromes(s: str) -> int:
    n = len(s)
    max_end = [1] * n
    max_start = [1] * n

    def expand(l, r):
        while l >= 0 and r < n and s[l] == s[r]:
            length = r - l + 1
            max_end[r] = max(max_end[r], length)
            max_start[l] = max(max_start[l], length)
            l -= 1
            r += 1

    for i in range(n):
        expand(i, i)

    prefix = [0] * n
    suffix = [0] * n

    prefix[0] = max_end[0]
    for i in range(1, n):
        prefix[i] = max(prefix[i-1], max_end[i])

    suffix[n-1] = max_start[n-1]
    for i in range(n - 2, -1, -1):
        suffix[i] = max(suffix[i+1], max_start[i])

    res = 0
    for i in range(n - 1):
        res = max(res, prefix[i] * suffix[i+1])

    return res