from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        s = set(bank)
        q = deque()
        q.append((start, 0))
        mp = {
            'a': "tcg",
            't': "acg",
            'c': "atg",
            'g': "atc"
        }
        while q:
            t, step = q.popleft()
            if t == end:
                return step
            for i, v in enumerate(t):
                for j in mp[v]:
                    next_mut = t[:i] + j + t[i+1:]
                    if next_mut in s:
                        q.append((next_mut, step + 1))
                        s.remove(next_mut)
        return -1