from collections import Counter

def find_substring(s, words):
    if not s or not words or not words[0]:
        return []
    wl, nw, tl = len(words[0]), len(words), len(words[0]) * len(words)
    wc = Counter(words)
    res = []
    for i in range(len(s) - tl + 1):
        seen = Counter()
        for j in range(i, i + tl, wl):
            w = s[j:j+wl]
            seen[w] += 1
            if seen[w] > wc[w]:
                break
        else:
            res.append(i)
    return res