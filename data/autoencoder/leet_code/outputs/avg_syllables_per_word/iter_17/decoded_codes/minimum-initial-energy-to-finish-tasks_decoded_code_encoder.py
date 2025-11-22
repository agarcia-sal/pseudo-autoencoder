from typing import List

class Solution:
    def minimumEffort(self, list_of_tasks: List[List[int]]) -> int:
        # Sort tasks based on descending order of (minimum_energy - actual_energy)
        list_of_tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        current_energy = 0
        required_initial_energy = 0

        for actual_energy, minimum_energy in list_of_tasks:
            if current_energy < minimum_energy:
                required_initial_energy += minimum_energy - current_energy
                current_energy = minimum_energy
            current_energy -= actual_energy

        return required_initial_energy