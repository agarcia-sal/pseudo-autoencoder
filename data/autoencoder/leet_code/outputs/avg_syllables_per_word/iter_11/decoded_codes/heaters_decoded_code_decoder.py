class Solution:
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        min_radius = 0
        j = 0
        for house in houses:
            while j < len(heaters) - 1 and abs(heaters[j] - house) >= abs(heaters[j + 1] - house):
                j += 1
            min_radius = max(min_radius, abs(heaters[j] - house))
        return min_radius