def findReplaceString(s, indices, sources, targets):
    sortRepls = sorted(zip(indices, sources, targets))
    res, prev = [], 0
    for i, src, tgt in sortRepls:
        res.append(s[prev:i])
        if s[i:i+len(src)] == src:
            res.append(tgt)
        else:
            res.append(s[i:i+len(src)])
        prev = i + len(src)
    res.append(s[prev:])
    return ''.join(res)