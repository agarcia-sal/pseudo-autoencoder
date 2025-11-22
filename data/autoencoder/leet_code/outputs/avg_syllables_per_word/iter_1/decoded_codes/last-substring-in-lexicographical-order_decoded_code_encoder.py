def max_substring(s):
    n = len(s)
    max_c = max(s)
    max_i = [i for i, c in enumerate(s) if c == max_c]
    max_sub = ""
    for i in max_i:
        cur_sub = s[i:]
        if cur_sub > max_sub:
            max_sub = cur_sub
    return max_sub