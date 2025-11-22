def is_subseq(s, t):
    it = iter(t)
    return all(c in it for c in s)

def find_longest_uncommon_subsequence(strs):
    strs.sort(key=lambda x: (-len(x), x))
    for i, word in enumerate(strs):
        if all(not is_subseq(word, other) for j, other in enumerate(strs) if i != j):
            return len(word)
    return -1