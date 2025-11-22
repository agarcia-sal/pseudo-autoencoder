from typing import List, Tuple

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Sort tasks by (minimum_energy - actual_energy) in descending order
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        current_energy = 0
        required_initial_energy = 0
        for actual_energy, minimum_energy in tasks:
            if current_energy < minimum_energy:
                required_initial_energy += minimum_energy - current_energy
                current_energy = minimum_energy
            current_energy -= actual_energy
        return required_initial_energy