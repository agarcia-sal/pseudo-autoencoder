def characterReplacement(s: str, k: int) -> int:
    max_len = 0
    max_cnt = 0
    left = 0
    count = {}

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_cnt = max(max_cnt, count[s[right]])

        if (right - left + 1) - max_cnt > k:
            count[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len