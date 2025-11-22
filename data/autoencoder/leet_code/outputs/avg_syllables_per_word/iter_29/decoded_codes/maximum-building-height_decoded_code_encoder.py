class Solution:
    def maxBuilding(self, n, restrictions):
        # Append position 1 with height 0 as a restriction
        restrictions.append([1, 0])
        # Sort restrictions by position
        restrictions.sort(key=lambda x: x[0])

        # Forward pass to ensure height constraints relative to previous position
        for i in range(1, len(restrictions)):
            curr_pos, curr_height = restrictions[i]
            prev_pos, prev_height = restrictions[i - 1]
            restrictions[i][1] = min(curr_height, prev_height + (curr_pos - prev_pos))

        # Backward pass to ensure height constraints relative to next position
        for i in range(len(restrictions) - 2, -1, -1):
            curr_pos, curr_height = restrictions[i]
            next_pos, next_height = restrictions[i + 1]
            restrictions[i][1] = min(curr_height, next_height + (next_pos - curr_pos))

        max_height = 0
        prev_pos, prev_height = restrictions[0]

        # Calculate maximum achievable height between restrictions
        for i in range(1, len(restrictions)):
            curr_pos, curr_height = restrictions[i]
            # The maximum height between two restrictions can be formed at midpoint
            calculated_height = (prev_height + curr_height + (curr_pos - prev_pos)) // 2
            if calculated_height > max_height:
                max_height = calculated_height
            prev_pos, prev_height = curr_pos, curr_height

        # Consider possible height increase after last restriction until position n
        max_height = max(max_height, prev_height + (n - prev_pos))

        return max_height