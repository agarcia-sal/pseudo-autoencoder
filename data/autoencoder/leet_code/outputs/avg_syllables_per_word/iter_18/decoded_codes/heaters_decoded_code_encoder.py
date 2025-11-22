from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        min_radius = 0
        pointer_j = 0
        for house in houses:
            while pointer_j < len(heaters) - 1 and abs(heaters[pointer_j] - house) >= abs(heaters[pointer_j + 1] - house):
                pointer_j += 1
            min_radius = max(min_radius, abs(heaters[pointer_j] - house))
        return min_radius