def find_radius(houses, heaters):
    houses.sort()
    heaters.sort()
    r = 0
    j = 0
    for house in houses:
        while j < len(heaters) - 1 and abs(heaters[j] - house) >= abs(heaters[j + 1] - house):
            j += 1
        r = max(r, abs(heaters[j] - house))
    return r