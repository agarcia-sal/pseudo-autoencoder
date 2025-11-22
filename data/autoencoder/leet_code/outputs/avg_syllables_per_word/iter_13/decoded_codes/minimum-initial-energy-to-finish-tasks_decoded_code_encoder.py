from typing import List, Tuple

class Solution:
    def minimumEffort(self, tasks: List[Tuple[int, int]]) -> int:
        # Sort tasks by (minimum - actual) in descending order
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        current_energy = 0
        required_initial_energy = 0
        for actual, minimum in tasks:
            if current_energy < minimum:
                required_initial_energy += minimum - current_energy
                current_energy = minimum
            current_energy -= actual
        return required_initial_energy