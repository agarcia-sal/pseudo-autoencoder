def find_permutation(s):
    res = list(range(1, len(s) + 2))
    start = 0
    for end in range(len(s) + 1):
        if end == len(s) or s[end] == 'I':
            res[start:end + 1] = reversed(res[start:end + 1])
            start = end + 1
    return res