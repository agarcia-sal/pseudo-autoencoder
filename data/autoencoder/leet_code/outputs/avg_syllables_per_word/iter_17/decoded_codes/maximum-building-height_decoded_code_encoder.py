class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        # Append the default restriction at building 1 with height 0
        restrictions.append([1, 0])
        restrictions.sort()

        # Forward pass to enforce height constraints
        for i in range(1, len(restrictions)):
            current_index, current_height = restrictions[i]
            prev_index, prev_height = restrictions[i - 1]
            allowed_height = prev_height + (current_index - prev_index)
            restrictions[i][1] = min(current_height, allowed_height)

        # Backward pass to enforce height constraints
        for i in range(len(restrictions) - 2, -1, -1):
            current_index, current_height = restrictions[i]
            next_index, next_height = restrictions[i + 1]
            allowed_height = next_height + (next_index - current_index)
            restrictions[i][1] = min(current_height, allowed_height)

        max_height = 0
        prev_index, prev_height = restrictions[0]

        # Find max possible height between restrictions
        for i in range(1, len(restrictions)):
            current_index, current_height = restrictions[i]
            dist = current_index - prev_index
            # The highest peak between two restricted buildings given their heights
            candidate = (prev_height + current_height + dist) // 2
            if candidate > max_height:
                max_height = candidate
            prev_index, prev_height = current_index, current_height

        # Consider the stretch from the last restriction to building n
        max_height = max(max_height, prev_height + (n - prev_index))

        return max_height