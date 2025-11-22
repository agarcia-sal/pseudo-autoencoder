from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()

        # Separate the indices of Radiant ('R') and Dire ('D') senators
        for i, senator in enumerate(senate):
            if senator == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        n = len(senate)

        # Simulate the banning rounds
        while radiant and dire:
            r_index = radiant.popleft()
            d_index = dire.popleft()

            # The senator with the smaller index bans the other and stays for the next round
            if r_index < d_index:
                radiant.append(r_index + n)
            else:
                dire.append(d_index + n)

        # Determine the winning party
        return "Radiant" if radiant else "Dire"