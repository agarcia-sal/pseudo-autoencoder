from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Initialize min_val and max_val from the first and last elements of the first and last arrays
        min_val = arrays[0][0]
        max_val = arrays[-1][-1]
        max_distance = 0

        # Iterate from the second array to the last array
        for i in range(1, len(arrays)):
            current_array = arrays[i]
            current_min = current_array[0]
            current_max = current_array[-1]

            # Update max_distance with the maximum of current max_distance,
            # abs(current_max - min_val), and abs(max_val - current_min)
            max_distance = max(
                max_distance,
                abs(current_max - min_val),
                abs(max_val - current_min)
            )

            # Update min_val and max_val
            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)

        return max_distance