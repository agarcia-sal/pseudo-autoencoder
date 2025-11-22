from math import inf

class Solution:
    def minimumFinishTime(self, tires, changeTime, numLaps):
        # min_times[i] holds the minimal total time to run i+1 consecutive laps without changing tires
        min_times = [inf] * 15

        # Precompute minimal running times for 1 to 15 consecutive laps for each tire
        for f, r in tires:
            total_time = 0
            lap_time = f
            for i in range(15):
                # Calculate lap time f * r^i for the i-th lap on the same tire
                lap_time = f * (r ** i)
                # If it becomes more expensive than changing tire and starting fresh with base f, break
                if lap_time > changeTime + f:
                    break
                total_time += lap_time
                # Track minimal total time for running i+1 consecutive laps without changing tires
                if total_time < min_times[i]:
                    min_times[i] = total_time

        # dp[i] = minimum time to complete i laps (including tires change times except for the last segment)
        dp = [inf] * (numLaps + 1)
        dp[0] = 0

        for i in range(1, numLaps + 1):
            # j is the length of last segment of laps done without changing tires
            for j in range(min(i, 15)):
                candidate_time = dp[i - j - 1] + min_times[j] + changeTime
                if candidate_time < dp[i]:
                    dp[i] = candidate_time

        # We subtract changeTime because the last segment doesn't need an extra tire change after finishing
        return dp[numLaps] - changeTime