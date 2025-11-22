from typing import List

class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        number_of_cities = len(flights)
        number_of_weeks = len(days[0]) if days else 0

        dp_array = [-1] * number_of_cities
        dp_array[0] = 0

        flight_graph = {city_index: [] for city_index in range(number_of_cities)}
        for departure_city in range(number_of_cities):
            for destination_city in range(number_of_cities):
                if flights[departure_city][destination_city] == 1:
                    flight_graph[departure_city].append(destination_city)

        for current_week in range(number_of_weeks):
            new_dp_array = [-1] * number_of_cities
            for current_city in range(number_of_cities):
                if dp_array[current_city] == -1:
                    continue

                # Stay in the current city
                new_dp_array[current_city] = max(new_dp_array[current_city], dp_array[current_city] + days[current_city][current_week])

                # Travel to reachable cities
                for reachable_city in flight_graph[current_city]:
                    new_dp_array[reachable_city] = max(new_dp_array[reachable_city], dp_array[current_city] + days[reachable_city][current_week])

            dp_array = new_dp_array

        return max(dp_array)