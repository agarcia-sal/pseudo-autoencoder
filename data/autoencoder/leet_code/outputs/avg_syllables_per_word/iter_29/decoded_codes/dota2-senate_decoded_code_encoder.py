from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        length_of_senate = len(senate)

        for index_position, senator_character in enumerate(senate):
            if senator_character == 'R':
                radiant.append(index_position)
            else:
                dire.append(index_position)

        while radiant and dire:
            radiant_index = radiant.popleft()
            dire_index = dire.popleft()

            if radiant_index < dire_index:
                radiant.append(radiant_index + length_of_senate)
            else:
                dire.append(dire_index + length_of_senate)

        if radiant:
            return "Radiant"
        else:
            return "Dire"