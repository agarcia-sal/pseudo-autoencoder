class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        list_of_position_and_speed = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        list_of_time_to_target = [(target - p) / s for p, s in list_of_position_and_speed]

        fleets = 0
        current_maximum_time = 0

        for time_value in list_of_time_to_target:
            if time_value > current_maximum_time:
                fleets += 1
                current_maximum_time = time_value

        return fleets