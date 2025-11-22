def wordsAbbreviation(words):
    def abbreviate(w, p):
        return w if len(w) - p <= 2 else w[:p] + str(len(w) - p - 1) + w[-1]

    def get_abbs(ws, p):
        map = {}
        for i, w in ws:
            map.setdefault(abbreviate(w, p), []).append((i, w))
        return map

    n = len(words)
    ans = [""] * n
    ws = [(i, w) for i, w in enumerate(words)]
    abbs = get_abbs(ws, 1)

    for abb, grp in abbs.items():
        if len(grp) == 1:
            i, w = grp[0]
            ans[i] = abb
        else:
            new_grp = grp
            p = 2
            while new_grp:
                new_abbs = get_abbs(new_grp, p)
                new_grp = []
                for a, g in new_abbs.items():
                    if len(g) == 1:
                        i, w = g[0]
                        ans[i] = a
                    else:
                        new_grp.extend(g)
                p += 1
    return ans