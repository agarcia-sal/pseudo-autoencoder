def length_of_longest_substring(s):
    char_map = {}
    max_len = 0
    start = 0
    for end, c in enumerate(s):
        if c in char_map and char_map[c] >= start:
            start = char_map[c] + 1
        char_map[c] = end
        max_len = max(max_len, end - start + 1)
    return max_len