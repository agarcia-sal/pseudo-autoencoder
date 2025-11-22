def addBoldTag(s, words):
    if not words:
        return s
    n = len(s)
    mask = [False] * n

    for w in words:
        start = 0
        while start <= n - len(w):
            start = s.find(w, start)
            if start == -1:
                break
            for i in range(start, start + len(w)):
                mask[i] = True
            start += 1

    res = []
    i = 0
    while i < n:
        if mask[i]:
            res.append("<b>")
            while i < n and mask[i]:
                res.append(s[i])
                i += 1
            res.append("</b>")
        else:
            res.append(s[i])
            i += 1

    return "".join(res)