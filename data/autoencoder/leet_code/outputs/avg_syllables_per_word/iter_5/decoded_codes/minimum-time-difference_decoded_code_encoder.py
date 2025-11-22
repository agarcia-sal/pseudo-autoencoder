class Solution:
    def findMinDifference(self, timePoints):
        def to_minutes(time):
            h, m = time.split(':')
            return int(h) * 60 + int(m)

        minutes_list = sorted(to_minutes(t) for t in timePoints)
        min_diff = float('inf')
        for i in range(1, len(minutes_list)):
            current_diff = minutes_list[i] - minutes_list[i - 1]
            if current_diff < min_diff:
                min_diff = current_diff

        circular_diff = 1440 - minutes_list[-1] + minutes_list[0]
        return min(min_diff, circular_diff)