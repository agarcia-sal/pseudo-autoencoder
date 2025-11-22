from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: t[1] - t[0], reverse=True)
        current_energy = 0
        required_initial_energy = 0
        for actual, minimum in tasks:
            if current_energy < minimum:
                required_initial_energy += minimum - current_energy
                current_energy = minimum
            current_energy -= actual
        return required_initial_energy