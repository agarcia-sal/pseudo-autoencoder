def longestSubstring(s, k):
    if len(s) < k:
        return 0
    from collections import Counter
    count = Counter(s)
    for c in count:
        if count[c] < k:
            return max(longestSubstring(sub, k) for sub in s.split(c))
    return len(s)