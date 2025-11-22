from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        length = len(senate)

        for i, senator in enumerate(senate):
            if senator == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r_index = radiant.popleft()
            d_index = dire.popleft()

            if r_index < d_index:
                radiant.append(r_index + length)
            else:
                dire.append(d_index + length)

        return "Radiant" if radiant else "Dire"