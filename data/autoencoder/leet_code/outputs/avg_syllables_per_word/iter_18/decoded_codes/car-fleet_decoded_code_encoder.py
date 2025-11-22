class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        zipped_pairs = zip(position, speed)
        sorted_pairs = sorted(zipped_pairs, key=lambda x: x[0], reverse=True)
        time_to_target = []
        for pos, spd in sorted_pairs:
            time_to_target.append((target - pos) / spd)
        fleets = 0
        current_max_time = 0.0
        for time in time_to_target:
            if time > current_max_time:
                fleets += 1
                current_max_time = time
        return fleets