from collections import Counter

def find_anagrams(s, p):
    len_s, len_p = len(s), len(p)
    if len_p > len_s:
        return []

    p_count = Counter(p)
    s_count = Counter(s[:len_p])
    ans = []

    if s_count == p_count:
        ans.append(0)

    for i in range(len_p, len_s):
        s_count[s[i]] += 1
        s_count[s[i - len_p]] -= 1
        if s_count[s[i - len_p]] == 0:
            del s_count[s[i - len_p]]
        if s_count == p_count:
            ans.append(i - len_p + 1)

    return ans