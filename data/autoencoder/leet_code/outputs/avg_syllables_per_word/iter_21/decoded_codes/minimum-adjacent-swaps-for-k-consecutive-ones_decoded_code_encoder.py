from typing import List

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        # Extract positions of all 1's in nums
        positions = [i for i, num in enumerate(nums) if num == 1]

        def calculate_cost(start: int, end: int) -> int:
            mid = (start + end) // 2
            median = positions[mid]
            cost = 0
            for index in range(start, end):
                offset = mid - index
                target_position = median - offset
                cost += abs(positions[index] - target_position)
            return cost

        min_cost = float('inf')
        for index in range(len(positions) - k + 1):
            current_cost = calculate_cost(index, index + k)
            if current_cost < min_cost:
                min_cost = current_cost

        return min_cost