def length_of_longest_substring_k_distinct(s, k):
    if k == 0:
        return 0
    map = {}
    left = 0
    maxLen = 0
    for right in range(len(s)):
        map[s[right]] = right
        if len(map) > k:
            leftChar = min(map, key=map.get)
            left = map.pop(leftChar) + 1
        maxLen = max(maxLen, right - left + 1)
    return maxLen