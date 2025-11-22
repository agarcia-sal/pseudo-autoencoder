class Solution:
    def findMinDifference(self, timePoints):
        def to_minutes(time):
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes

        minutes_list = sorted(to_minutes(t) for t in timePoints)

        min_diff = float('inf')
        for i in range(1, len(minutes_list)):
            diff = minutes_list[i] - minutes_list[i - 1]
            if diff < min_diff:
                min_diff = diff

        circular_diff = (1440 - minutes_list[-1]) + minutes_list[0]
        if circular_diff < min_diff:
            min_diff = circular_diff

        return min_diff