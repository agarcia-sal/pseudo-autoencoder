class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()

        for i in range(1, len(restrictions)):
            curr_idx, curr_height = restrictions[i]
            prev_idx, prev_height = restrictions[i - 1]
            restrictions[i][1] = min(curr_height, prev_height + curr_idx - prev_idx)

        for i in range(len(restrictions) - 2, -1, -1):
            curr_idx, curr_height = restrictions[i]
            next_idx, next_height = restrictions[i + 1]
            restrictions[i][1] = min(curr_height, next_height + next_idx - curr_idx)

        max_height = 0
        prev_idx, prev_height = restrictions[0]

        for i in range(1, len(restrictions)):
            curr_idx, curr_height = restrictions[i]
            candidate = (curr_idx - prev_idx + prev_height + curr_height) // 2
            if candidate > max_height:
                max_height = candidate
            prev_idx, prev_height = curr_idx, curr_height

        candidate = prev_height + n - prev_idx
        if candidate > max_height:
            max_height = candidate

        return max_height