class Solution:
    def findMinDifference(self, timePoints):
        def to_minutes(time):
            h, m = map(int, time.split(':'))
            return h * 60 + m

        minutes_list = sorted(map(to_minutes, timePoints))
        min_diff = float('inf')

        for i in range(1, len(minutes_list)):
            diff = minutes_list[i] - minutes_list[i - 1]
            if diff < min_diff:
                min_diff = diff

        circular_diff = (1440 - minutes_list[-1]) + minutes_list[0]
        return min(min_diff, circular_diff)