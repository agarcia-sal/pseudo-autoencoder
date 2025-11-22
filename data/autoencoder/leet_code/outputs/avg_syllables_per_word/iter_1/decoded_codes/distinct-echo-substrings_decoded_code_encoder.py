def count_repeated_substrings(text):
    n = len(text)
    subs = set()
    for L in range(1, n // 2 + 1):
        for i in range(n - 2 * L + 1):
            if text[i:i + L] == text[i + L:i + 2 * L]:
                subs.add(text[i:i + 2 * L])
    return len(subs)