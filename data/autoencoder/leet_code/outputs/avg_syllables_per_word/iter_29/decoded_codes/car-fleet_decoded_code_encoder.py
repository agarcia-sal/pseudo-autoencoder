from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        list_of_pairs = list(zip(position, speed))
        list_of_pairs.sort(key=lambda x: x[0], reverse=True)
        list_of_times = [(target - pos) / spd for pos, spd in list_of_pairs]

        fleet_count = 0
        current_maximum_time = 0.0
        for time_value in list_of_times:
            if time_value > current_maximum_time:
                fleet_count += 1
                current_maximum_time = time_value
        return fleet_count