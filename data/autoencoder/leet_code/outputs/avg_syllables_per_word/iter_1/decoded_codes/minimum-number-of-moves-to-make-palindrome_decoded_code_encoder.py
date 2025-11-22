def minMovesToMakePalindrome(s):
    s = list(s)
    m = 0
    while len(s) > 1:
        for i in range(len(s)-1, 0, -1):
            if s[i] == s[0]:
                for j in range(i, len(s)-1):
                    s[j], s[j+1] = s[j+1], s[j]
                    m += 1
                s.pop(0)
                s.pop()
                break
        else:
            s.pop(0)
    return m