class Solution:
    def findMinDifference(self, timePoints):
        def to_minutes(time):
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes

        minutes_list = list(map(to_minutes, timePoints))
        minutes_list.sort()

        min_diff = float('inf')
        for i in range(1, len(minutes_list)):
            current_difference = minutes_list[i] - minutes_list[i - 1]
            if current_difference < min_diff:
                min_diff = current_difference

        circular_difference = 1440 - minutes_list[-1] + minutes_list[0]
        if circular_difference < min_diff:
            min_diff = circular_difference

        return min_diff