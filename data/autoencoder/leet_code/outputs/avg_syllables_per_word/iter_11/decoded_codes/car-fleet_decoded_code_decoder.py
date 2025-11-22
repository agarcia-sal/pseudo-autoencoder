class Solution:
    def carFleet(self, target, position, speed):
        pairs = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        time_to_target = []
        for pos, spd in pairs:
            time_value = (target - pos) / spd
            time_to_target.append(time_value)
        fleets = 0
        current_max_time = 0
        for time_element in time_to_target:
            if time_element > current_max_time:
                fleets += 1
                current_max_time = time_element
        return fleets