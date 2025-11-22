def shortestPalindrome(s):
    if not s:
        return s
    for i in range(len(s), -1, -1):
        if s[:i] == s[:i][::-1]:
            return s[i:][::-1] + s