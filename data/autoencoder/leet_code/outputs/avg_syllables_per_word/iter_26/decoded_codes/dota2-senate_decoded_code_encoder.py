from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()

        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        n = len(senate)
        while radiant and dire:
            radiant_index = radiant.popleft()
            dire_index = dire.popleft()
            if radiant_index < dire_index:
                radiant.append(radiant_index + n)
            else:
                dire.append(dire_index + n)

        return "Radiant" if radiant else "Dire"