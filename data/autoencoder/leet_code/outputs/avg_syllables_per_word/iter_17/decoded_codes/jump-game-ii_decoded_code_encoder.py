from typing import List

class Solution:
    def jump(self, list_of_numbers: List[int]) -> int:
        if len(list_of_numbers) <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        for index in range(len(list_of_numbers) - 1):
            farthest = max(farthest, index + list_of_numbers[index])

            if index == current_end:
                jumps += 1
                current_end = farthest

                if current_end >= len(list_of_numbers) - 1:
                    break

        return jumps