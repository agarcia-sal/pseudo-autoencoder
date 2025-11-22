from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        self.sortTasksDescendingByDifference(tasks)
        current_energy = 0
        required_initial_energy = 0
        for task in tasks:
            actual = task[0]
            minimum = task[1]
            if current_energy < minimum:
                required_initial_energy += minimum - current_energy
                current_energy = minimum
            current_energy -= actual
        return required_initial_energy

    def sortTasksDescendingByDifference(self, tasks: List[List[int]]) -> None:
        # sort in-place by descending (minimum - actual)
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)