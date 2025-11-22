def largestPalindrome(n):
    if n == 1:
        return 9
    u = 10**n - 1
    l = 10**(n-1)
    maxP = 0
    for i in range(u, l - 1, -1):
        for j in range(i, l - 1, -1):
            p = i * j
            if p <= maxP:
                break
            if str(p) == str(p)[::-1]:
                maxP = p
    return maxP % 1337