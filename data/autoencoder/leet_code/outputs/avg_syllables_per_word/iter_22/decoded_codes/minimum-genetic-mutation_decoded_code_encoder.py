from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        s = set(bank)
        q = deque([(start, 0)])
        mp = {
            'A': "TCG",
            'T': "ACG",
            'C': "ATG",
            'G': "ATC"
        }
        while q:
            t, step = q.popleft()
            if t == end:
                return step
            for i, v in enumerate(t):
                for j in mp[v]:
                    next_ = t[:i] + j + t[i+1:]
                    if next_ in s:
                        q.append((next_, step + 1))
                        s.remove(next_)
        return -1