class Solution:
    def minMoves(self, nums: list[int], k: int) -> int:
        positions = []
        for i in range(len(nums)):
            if nums[i] == 1:
                positions.append(i)

        def calculate_cost(start: int, end: int) -> int:
            mid = (start + end) // 2
            median = positions[mid]
            cost = 0
            for i in range(start, end):
                distance = positions[i] - median + (mid - i)
                if distance < 0:
                    distance = -distance
                cost += distance
            return cost

        min_cost = float('inf')
        for i in range(len(positions) - k + 1):
            current_cost = calculate_cost(i, i + k)
            if current_cost < min_cost:
                min_cost = current_cost

        return min_cost