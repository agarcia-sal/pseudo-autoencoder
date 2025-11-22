class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        # Append the first building with height zero
        restrictions.append([1, 0])
        # Sort restrictions by position
        restrictions.sort(key=lambda x: x[0])

        # Forward pass to enforce height restrictions with difference constraints
        for i in range(1, len(restrictions)):
            curr_index, curr_height = restrictions[i]
            prev_index, prev_height = restrictions[i - 1]
            restrictions[i][1] = min(curr_height, prev_height + (curr_index - prev_index))

        # Backward pass to enforce height restrictions with difference constraints
        for i in range(len(restrictions) - 2, -1, -1):
            curr_index, curr_height = restrictions[i]
            next_index, next_height = restrictions[i + 1]
            restrictions[i][1] = min(curr_height, next_height + (next_index - curr_index))

        max_height = 0
        prev_index, prev_height = restrictions[0]
        for i in range(1, len(restrictions)):
            curr_index, curr_height = restrictions[i]
            # Calculate max possible height between two restrictions
            dist = curr_index - prev_index
            possible_height = (prev_height + curr_height + dist) // 2
            max_height = max(max_height, possible_height)
            prev_index, prev_height = curr_index, curr_height

        max_height = max(max_height, prev_height + (n - prev_index))
        return max_height