from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        total_operations = 0
        previous_number = 0
        for current_number in target:
            if current_number > previous_number:
                total_operations += current_number - previous_number
            previous_number = current_number
        return total_operations