from typing import List

class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        number_of_cities = len(flights)
        number_of_weeks = len(days[0]) if days else 0

        dp_list = [-1] * number_of_cities
        dp_list[0] = 0

        graph_dictionary = {city_index: [] for city_index in range(number_of_cities)}
        for city_index in range(number_of_cities):
            for destination_index in range(number_of_cities):
                if flights[city_index][destination_index] == 1:
                    graph_dictionary[city_index].append(destination_index)

        for week_index in range(number_of_weeks):
            new_dp_list = [-1] * number_of_cities
            for city_index in range(number_of_cities):
                if dp_list[city_index] == -1:
                    continue
                current_vacation = dp_list[city_index]

                # Stay in the same city
                new_dp_list[city_index] = max(new_dp_list[city_index], current_vacation + days[city_index][week_index])

                # Travel to reachable cities
                for reachable_city in graph_dictionary[city_index]:
                    new_dp_list[reachable_city] = max(new_dp_list[reachable_city], current_vacation + days[reachable_city][week_index])

            dp_list = new_dp_list

        return max(dp_list) if dp_list else 0