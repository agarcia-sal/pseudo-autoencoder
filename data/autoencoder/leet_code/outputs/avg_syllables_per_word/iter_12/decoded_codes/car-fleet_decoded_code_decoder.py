class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        paired_list = sorted(zip(position, speed), reverse=True)
        time_to_target = [(target - pos) / spd for pos, spd in paired_list]

        fleets = 0
        current_max_time = 0.0

        for time_element in time_to_target:
            if time_element > current_max_time:
                fleets += 1
                current_max_time = time_element

        return fleets