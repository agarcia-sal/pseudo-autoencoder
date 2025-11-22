from collections import defaultdict, deque
from typing import List

class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        number_of_elements = len(nums)
        graph = defaultdict(list)
        indegree_list = [0] * (number_of_elements + 1)

        for sequence in sequences:
            for position in range(len(sequence) - 1):
                first_element = sequence[position]
                second_element = sequence[position + 1]
                graph[first_element].append(second_element)
                indegree_list[second_element] += 1

        queue = deque(i for i in range(1, number_of_elements + 1) if indegree_list[i] == 0)

        if len(queue) != 1:
            return False

        current_index = 0
        while queue:
            if len(queue) != 1:
                return False

            current_node = queue.popleft()
            if current_node != nums[current_index]:
                return False
            current_index += 1

            for adjacent_node in graph[current_node]:
                indegree_list[adjacent_node] -= 1
                if indegree_list[adjacent_node] == 0:
                    queue.append(adjacent_node)

        return current_index == number_of_elements