from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        s = set(bank)
        if end not in s:
            return -1
        q = deque([(start, 0)])
        mp = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}

        while q:
            t, step = q.popleft()
            if t == end:
                return step
            for i, v in enumerate(t):
                for j in mp[v]:
                    next_seq = t[:i] + j + t[i+1:]
                    if next_seq in s:
                        q.append((next_seq, step + 1))
                        s.remove(next_seq)
        return -1