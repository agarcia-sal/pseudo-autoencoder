from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        min_radius = 0
        j = 0
        for house in houses:
            while j < len(heaters) - 1 and abs(heaters[j] - house) >= abs(heaters[j + 1] - house):
                j += 1
            current_distance = abs(heaters[j] - house)
            if current_distance > min_radius:
                min_radius = current_distance
        return min_radius