def nearest_palindrome(n: str) -> str:
    length = len(n)
    if length == 1:
        return str(int(n) - 1)

    cands = {10 ** length + 1, 10 ** (length - 1) - 1}

    pref = int(n[: (length + 1) // 2])

    for i in [-1, 0, 1]:
        p = str(pref + i)
        if length % 2 == 0:
            cand = p + p[::-1]
        else:
            cand = p + p[:-1][::-1]
        cands.add(int(cand))

    cands.discard(int(n))

    closest = min(cands, key=lambda x: (abs(x - int(n)), x))
    return str(closest)