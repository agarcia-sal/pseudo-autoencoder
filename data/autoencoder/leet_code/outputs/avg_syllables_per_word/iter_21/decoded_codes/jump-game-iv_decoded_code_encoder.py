from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n == 1:
            return 0

        value_indices = self.create_value_indices(arr)
        queue = self.create_queue(0, 0)
        visited = self.create_visited(0)

        while queue:
            current_index, steps = self.dequeue_from_queue(queue)

            if current_index == n - 1:
                return steps

            next_indices = self.assemble_next_indices(current_index, n, value_indices, arr)

            for next_index in next_indices:
                if 0 <= next_index < n and next_index not in visited:
                    visited.add(next_index)
                    self.enqueue_to_queue(queue, next_index, steps + 1)

            self.clear_value_indices_for_value(value_indices, arr, current_index)

        return -1

    def create_value_indices(self, arr):
        value_indices = defaultdict(list)
        for pos, val in enumerate(arr):
            value_indices[val].append(pos)
        return value_indices

    def create_queue(self, starting_index, starting_steps):
        return deque([(starting_index, starting_steps)])

    def create_visited(self, starting_index):
        return set([starting_index])

    def dequeue_from_queue(self, queue):
        return queue.popleft()

    def assemble_next_indices(self, current_index, n, value_indices, arr):
        next_indices = [current_index + 1, current_index - 1]
        next_indices.extend(value_indices[arr[current_index]])
        return next_indices

    def enqueue_to_queue(self, queue, next_index, next_steps):
        queue.append((next_index, next_steps))

    def clear_value_indices_for_value(self, value_indices, arr, current_index):
        value_indices[arr[current_index]] = []