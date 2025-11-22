class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        time_to_target = [(target - p) / s for p, s in cars]

        fleets = 0
        current_max_time = 0
        for time in time_to_target:
            if time > current_max_time:
                fleets += 1
                current_max_time = time
        return fleets