class Solution:
    def minMoves(self, nums: list[int], k: int) -> int:
        positions = [i for i, val in enumerate(nums) if val == 1]

        def calculate_cost(start: int, end: int) -> int:
            mid = (start + end) // 2
            median = positions[mid]
            cost = 0
            for idx in range(start, end):
                distance = abs(positions[idx] - median) - abs(mid - idx)
                cost += distance
            return cost

        min_cost = float('inf')
        for i in range(len(positions) - k + 1):
            current_cost = calculate_cost(i, i + k)
            if current_cost < min_cost:
                min_cost = current_cost

        return min_cost