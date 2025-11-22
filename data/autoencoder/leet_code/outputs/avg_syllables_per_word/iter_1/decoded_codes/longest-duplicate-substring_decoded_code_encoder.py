def longestDupSubstring(s):
    def search(length):
        seen = set()
        for i in range(len(s) - length + 1):
            sub = s[i:i+length]
            if sub in seen:
                return sub
            seen.add(sub)
        return ""

    left, right, longest = 1, len(s) - 1, ""
    while left <= right:
        mid = (left + right) // 2
        cand = search(mid)
        if cand != "":
            longest = cand
            left = mid + 1
        else:
            right = mid - 1
    return longest