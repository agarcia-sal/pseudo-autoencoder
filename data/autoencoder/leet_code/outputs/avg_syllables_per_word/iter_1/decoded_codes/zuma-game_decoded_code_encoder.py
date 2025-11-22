from collections import Counter
import copy

def clean(b):
    s = []
    for c in b:
        if s and s[-1][0] != c and s[-1][1] >= 3:
            s.pop()
        if not s or s[-1][0] != c:
            s.append([c, 1])
        else:
            s[-1][1] += 1
    if s and s[-1][1] >= 3:
        s.pop()
    return "".join(c * cnt for c, cnt in s)

def dfs(b, h):
    if not b:
        return 0
    res = float('inf')
    i = 0
    while i < len(b):
        j = i + 1
        while j < len(b) and b[i] == b[j]:
            j += 1
        need = 3 - (j - i)
        if h[b[i]] >= need:
            newh = copy.deepcopy(h)
            newh[b[i]] -= need
            nb = clean(b[:i] + b[j:])
            steps = dfs(nb, newh)
            if steps >= 0:
                res = min(res, steps + need)
        i = j
    return res if res != float('inf') else -1

# Example usage:
# board = "WRRBBW"
# hand = "RB"
# count = Counter(hand)
# print(dfs(board, count))