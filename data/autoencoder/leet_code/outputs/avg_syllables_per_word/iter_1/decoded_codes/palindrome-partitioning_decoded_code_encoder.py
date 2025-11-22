def is_pal(s):
    return s == s[::-1]

def backtrack(i, p):
    if i == len(s):
        res.append(p)
        return
    for j in range(i + 1, len(s) + 1):
        if is_pal(s[i:j]):
            backtrack(j, p + [s[i:j]])

def palindrome_partitions(s):
    global res
    res = []
    backtrack(0, [])
    return res