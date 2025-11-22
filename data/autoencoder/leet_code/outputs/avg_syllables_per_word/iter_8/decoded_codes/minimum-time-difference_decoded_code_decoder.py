class Solution:
    def findMinDifference(self, timePoints):
        def to_minutes(time):
            hours, minutes = time.split(':')
            hours = int(hours)
            minutes = int(minutes)
            return hours * 60 + minutes

        minutes_list = list(map(to_minutes, timePoints))
        minutes_list.sort()
        min_diff = float('inf')

        for i in range(1, len(minutes_list)):
            current_diff = minutes_list[i] - minutes_list[i - 1]
            if current_diff < min_diff:
                min_diff = current_diff

        circular_diff = (1440 - minutes_list[-1]) + minutes_list[0]
        if circular_diff < min_diff:
            min_diff = circular_diff

        return min_diff