from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        length_of_arr = len(arr)
        if length_of_arr == 1:
            return 0

        value_indices = defaultdict(list)
        for position_index, element_value in enumerate(arr):
            value_indices[element_value].append(position_index)

        queue = deque([(0, 0)])
        visited = {0}

        while queue:
            current_index, steps = queue.popleft()
            if current_index == length_of_arr - 1:
                return steps

            next_indices = [current_index - 1, current_index + 1] + value_indices[arr[current_index]]

            for next_index in next_indices:
                if 0 <= next_index < length_of_arr and next_index not in visited:
                    visited.add(next_index)
                    queue.append((next_index, steps + 1))

            value_indices[arr[current_index]].clear()

        return -1