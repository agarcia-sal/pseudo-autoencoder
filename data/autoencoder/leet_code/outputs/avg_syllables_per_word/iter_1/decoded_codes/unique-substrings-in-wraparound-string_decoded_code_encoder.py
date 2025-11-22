def consecutive_letters_string(s: str) -> int:
    max_len = {chr(c): 0 for c in range(ord('a'), ord('z')+1)}
    cur_len = 0
    for i in range(len(s)):
        if i > 0 and (ord(s[i]) - ord(s[i-1]) == 1 or (s[i] == 'a' and s[i-1] == 'z')):
            cur_len += 1
        else:
            cur_len = 1
        max_len[s[i]] = max(max_len[s[i]], cur_len)
    return sum(max_len.values())