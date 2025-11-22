from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant, dire = deque(), deque()
        n = len(senate)
        for i, s in enumerate(senate):
            (radiant if s == 'R' else dire).append(i)
        while radiant and dire:
            r_index, d_index = radiant.popleft(), dire.popleft()
            if r_index < d_index:
                radiant.append(r_index + n)
            else:
                dire.append(d_index + n)
        return "Radiant" if radiant else "Dire"