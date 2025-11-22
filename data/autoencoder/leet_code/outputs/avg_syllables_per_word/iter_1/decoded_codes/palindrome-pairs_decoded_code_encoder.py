def palindromePairs(words):
    word_idx = {w: i for i, w in enumerate(words)}
    res = []

    def is_pal(s):
        return s == s[::-1]

    for i, w in enumerate(words):
        if w == "":
            continue

        if "" in word_idx and is_pal(w):
            res.append([i, word_idx[""]])
            res.append([word_idx[""], i])

        rev_w = w[::-1]
        if rev_w in word_idx and word_idx[rev_w] != i:
            res.append([i, word_idx[rev_w]])

        for j in range(1, len(w)):
            p, s = w[:j], w[j:]
            rp, rs = p[::-1], s[::-1]

            if is_pal(s) and rp in word_idx:
                res.append([i, word_idx[rp]])
            if is_pal(p) and rs in word_idx:
                res.append([word_idx[rs], i])

    return res