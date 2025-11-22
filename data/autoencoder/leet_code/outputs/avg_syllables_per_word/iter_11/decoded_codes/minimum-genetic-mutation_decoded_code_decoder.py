from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        s = set(bank)
        q = deque()
        q.append((start, 0))
        mp = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}

        while q:
            t, step = q.popleft()
            if t == end:
                return step
            for i in range(len(t)):
                v = t[i]
                for j in mp[v]:
                    next_str = t[:i] + j + t[i+1:]
                    if next_str in s:
                        q.append((next_str, step + 1))
                        s.remove(next_str)
        return -1