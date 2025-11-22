from collections import Counter

score = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}
letter_cnt = Counter()  # This should be initialized before use, probably with letters available

def w_score(w):
    return sum(score[c] for c in w)

def can_make(w):
    w_count = Counter(w)
    return all(letter_cnt[c] >= freq for c, freq in w_count.items())

def upd_cnt(w, add):
    delta = 1 if add else -1
    for c in w:
        letter_cnt[c] += delta

def bt(i, cur, words):
    if i == len(words):
        return cur
    res = cur
    for j in range(i, len(words)):
        if can_make(words[j]):
            upd_cnt(words[j], False)
            res = max(res, bt(j + 1, cur + w_score(words[j]), words))
            upd_cnt(words[j], True)
    return res