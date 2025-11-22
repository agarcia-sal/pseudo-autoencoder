def find_min_difference(timePoints):
    def to_min(time):
        return int(time[:2]) * 60 + int(time[3:])
    mins = sorted(map(to_min, timePoints))
    min_diff = min(mins[i] - mins[i-1] for i in range(1, len(mins)))
    min_diff = min(min_diff, (1440 - mins[-1]) + mins[0])
    return min_diff