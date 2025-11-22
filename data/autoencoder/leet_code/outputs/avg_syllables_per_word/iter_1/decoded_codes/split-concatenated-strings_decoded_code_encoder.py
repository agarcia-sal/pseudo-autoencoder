def reverse(s):
    return s[::-1]

def max_lex_string(strs):
    for i in range(len(strs)):
        if reverse(strs[i]) > strs[i]:
            strs[i] = reverse(strs[i])

    doubled = strs + strs
    max_str = ""

    for i in range(len(strs)):
        for rev in [False, True]:
            cur = reverse(strs[i]) if rev else strs[i]
            rem = "".join(doubled[i+1 : i+len(strs)])
            for j in range(len(cur)):
                cand = cur[j:] + rem + cur[:j]
                if cand > max_str:
                    max_str = cand

    return max_str