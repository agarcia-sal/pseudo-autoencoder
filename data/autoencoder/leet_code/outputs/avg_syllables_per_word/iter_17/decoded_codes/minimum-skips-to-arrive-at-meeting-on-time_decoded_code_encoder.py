import math
from typing import List

class Solution:
    def minSkips(self, list_of_distances: List[int], speed: int, hours_before: int) -> int:
        number_of_roads = len(list_of_distances)
        INF = float('inf')
        dp = [[INF] * (number_of_roads + 1) for _ in range(number_of_roads)]

        total_distance = sum(list_of_distances)
        if total_distance / speed > hours_before:
            return -1

        dp[0][0] = list_of_distances[0]
        for skip_count in range(1, number_of_roads):
            dp[0][skip_count] = list_of_distances[0]

        for road_index in range(1, number_of_roads):
            for skip_count in range(0, road_index + 1):
                if skip_count < road_index:
                    prev_time = dp[road_index - 1][skip_count]
                    # Calculate the ceiling division to the nearest next multiple of speed
                    wait_time = math.ceil(prev_time / speed) * speed + list_of_distances[road_index]
                    dp[road_index][skip_count] = wait_time
                if skip_count > 0:
                    dp[road_index][skip_count] = min(
                        dp[road_index][skip_count],
                        dp[road_index - 1][skip_count - 1] + list_of_distances[road_index]
                    )

        for skip_count in range(number_of_roads):
            if dp[number_of_roads - 1][skip_count] <= hours_before * speed:
                return skip_count
        return -1