from collections import deque

class Solution:
    def minMutation(self, start, end, bank):
        s = set(bank)
        q = deque([(start, 0)])
        mp = {'A': "TCG", 'T': "ACG", 'C': "ATG", 'G': "ATC"}
        while q:
            t, step = q.popleft()
            if t == end:
                return step
            for i, v in enumerate(t):
                for j in mp[v]:
                    next_str = t[:i] + j + t[i+1:]
                    if next_str in s:
                        q.append((next_str, step + 1))
                        s.remove(next_str)
        return -1