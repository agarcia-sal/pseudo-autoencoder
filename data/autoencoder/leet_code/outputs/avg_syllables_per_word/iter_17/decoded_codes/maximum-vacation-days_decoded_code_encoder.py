from collections import defaultdict
from typing import List

class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        number_of_cities = len(flights)
        number_of_weeks = len(days[0])

        dp = [-1] * number_of_cities
        dp[0] = 0

        graph = defaultdict(list)
        for city_index in range(number_of_cities):
            for destination_index in range(number_of_cities):
                if flights[city_index][destination_index] == 1:
                    graph[city_index].append(destination_index)

        for week_index in range(number_of_weeks):
            new_dp = [-1] * number_of_cities

            for city_index in range(number_of_cities):
                if dp[city_index] == -1:
                    continue

                # Stay in current city
                new_dp[city_index] = max(new_dp[city_index], dp[city_index] + days[city_index][week_index])

                # Fly to reachable cities
                for reachable_city in graph[city_index]:
                    new_dp[reachable_city] = max(new_dp[reachable_city], dp[city_index] + days[reachable_city][week_index])

            dp = new_dp

        return max(dp)