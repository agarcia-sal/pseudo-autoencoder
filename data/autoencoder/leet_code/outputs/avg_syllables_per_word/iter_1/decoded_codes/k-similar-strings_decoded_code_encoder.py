from collections import deque

def kSimilarity(s1, s2):
    def neighbors(s):
        i = 0
        while i < len(s) and s[i] == s2[i]:
            i += 1
        for j in range(i + 1, len(s)):
            if s[j] == s2[i] and s[j] != s2[j]:
                lst = list(s)
                lst[i], lst[j] = lst[j], lst[i]
                yield ''.join(lst)

    queue = deque([(s1, 0)])
    visited = {s1}

    while queue:
        s, swaps = queue.popleft()
        if s == s2:
            return swaps
        for n in neighbors(s):
            if n not in visited:
                visited.add(n)
                queue.append((n, swaps + 1))