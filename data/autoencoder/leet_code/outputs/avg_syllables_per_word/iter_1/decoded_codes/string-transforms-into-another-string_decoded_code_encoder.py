def compare_strings(str1, str2):
    if str1 == str2:
        return True
    mapping = {}
    for c1, c2 in zip(str1, str2):
        if c1 in mapping and mapping[c1] != c2:
            return False
        mapping[c1] = c2
    if len(set(str2)) == 26:
        return False
    return True