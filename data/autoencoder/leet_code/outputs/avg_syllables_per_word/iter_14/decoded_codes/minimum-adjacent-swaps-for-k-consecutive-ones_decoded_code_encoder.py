class Solution:
    def minMoves(self, nums: list[int], k: int) -> int:
        positions = self.extract_positions(nums)

        def calculate_cost(start: int, end: int) -> int:
            mid = (start + end) // 2
            median = positions[mid]
            cost = 0
            for i in range(start, end):
                offset = median - (mid - i)
                distance = abs(positions[i] - offset)
                cost += distance
            return cost

        min_cost = float('inf')
        limit = len(positions) - k + 1
        for i in range(limit):
            current_cost = calculate_cost(i, i + k)
            if current_cost < min_cost:
                min_cost = current_cost

        return min_cost

    def extract_positions(self, nums: list[int]) -> list[int]:
        result = []
        for index, num in enumerate(nums):
            if num == 1:
                result.append(index)
        return result