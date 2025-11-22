def compress(w):
    if not w:
        return []
    c = 1
    res = []
    for i in range(1, len(w)):
        if w[i] == w[i - 1]:
            c += 1
        else:
            res.append((w[i - 1], c))
            c = 1
    res.append((w[-1], c))
    return res

def is_stretchy(s_c, w_c):
    if len(s_c) != len(w_c):
        return False
    for (sc, sc_ct), (wc, wc_ct) in zip(s_c, w_c):
        if sc != wc:
            return False
        if sc_ct != wc_ct and (sc_ct < 3 or sc_ct < wc_ct):
            return False
    return True

def expressiveWords(s, words):
    s_c = compress(s)
    cnt = 0
    for w in words:
        if is_stretchy(s_c, compress(w)):
            cnt += 1
    return cnt