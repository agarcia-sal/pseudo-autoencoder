class Solution:
    def minMoves(self, list_of_numbers, k):
        list_of_positions = [i for i, num in enumerate(list_of_numbers) if num == 1]

        def calculate_cost(start, end):
            mid = (start + end) // 2
            median = list_of_positions[mid]
            cost = 0
            for i in range(start, end):
                cost += abs(list_of_positions[i] - median - (mid - i))
            return cost

        minimal_cost = float('inf')
        length = len(list_of_positions)
        for i in range(length - k + 1):
            minimal_cost = min(minimal_cost, calculate_cost(i, i + k))

        return minimal_cost