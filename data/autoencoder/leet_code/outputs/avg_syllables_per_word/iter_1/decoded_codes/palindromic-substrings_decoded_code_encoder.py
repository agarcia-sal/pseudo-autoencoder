def countSubstrings(s):
    def expand(l, r):
        c = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            c += 1
            l -= 1
            r += 1
        return c
    total = 0
    for i in range(len(s)):
        total += expand(i, i) + expand(i, i + 1)
    return total