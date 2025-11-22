from collections import deque, defaultdict

class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n == 1:
            return 0

        value_indices = self.create_value_indices(arr)
        queue = self.create_queue(0, 0)
        visited = self.create_set(0)

        while queue:
            current_index, steps = self.dequeue_left(queue)

            if current_index == n - 1:
                return steps

            next_indices = self.get_next_indices(current_index, n, value_indices, arr)
            for next_index in next_indices:
                if 0 <= next_index < n and next_index not in visited:
                    self.add_to_set(next_index, visited)
                    self.enqueue_right(next_index, steps + 1, queue)

            self.clear_value_indices(current_index, value_indices, arr)

        return -1

    def create_value_indices(self, arr):
        value_indices = defaultdict(list)
        for index, value in enumerate(arr):
            value_indices[value].append(index)
        return value_indices

    def create_queue(self, start_index, start_steps):
        queue = deque()
        queue.append((start_index, start_steps))
        return queue

    def create_set(self, initial_element):
        return {initial_element}

    def dequeue_left(self, queue):
        return queue.popleft()

    def get_next_indices(self, current_index, n, value_indices, arr):
        next_indices = [current_index + 1, current_index - 1]
        value = arr[current_index]
        next_indices.extend(value_indices.get(value, []))
        return next_indices

    def add_to_set(self, element, set_collection):
        set_collection.add(element)

    def enqueue_right(self, element, steps, queue):
        queue.append((element, steps))

    def clear_value_indices(self, current_index, value_indices, arr):
        value = arr[current_index]
        value_indices[value] = []