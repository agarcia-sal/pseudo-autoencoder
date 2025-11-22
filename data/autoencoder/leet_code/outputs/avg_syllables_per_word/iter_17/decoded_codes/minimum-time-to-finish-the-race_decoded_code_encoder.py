from math import inf

class Solution:
    def minimumFinishTime(self, tires, changeTime, numLaps):
        min_times = initialize_minimum_times(15)  # min_times[i] = min time to run i+1 consecutive laps on the same tire

        for first_time, lap_multiplier in tires:
            total_time = 0
            for lap_index in range(15):
                lap_time = calculate_lap_time(first_time, lap_multiplier, lap_index)
                if lap_time > changeTime + first_time:
                    break
                total_time += lap_time
                if total_time < min_times[lap_index]:
                    min_times[lap_index] = total_time

        dp = initialize_dp(numLaps + 1)
        dp[0] = 0

        for i in range(1, numLaps + 1):
            for j in range(min(i, 15)):
                time = dp[i - j - 1] + min_times[j] + changeTime
                if time < dp[i]:
                    dp[i] = time

        return dp[numLaps] - changeTime


def initialize_minimum_times(length):
    return [inf] * length


def calculate_lap_time(first_time_multiplier, lap_multiplier, lap_index):
    return first_time_multiplier * (lap_multiplier ** lap_index)


def initialize_dp(length):
    return [inf] * length