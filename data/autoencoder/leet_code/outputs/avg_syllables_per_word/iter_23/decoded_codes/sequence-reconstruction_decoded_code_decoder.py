from collections import defaultdict, deque
from typing import List

class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        graph = defaultdict(list)
        indegree = [0] * (n + 1)

        for sequence in sequences:
            for i in range(len(sequence) - 1):
                u = sequence[i]
                v = sequence[i + 1]
                graph[u].append(v)
                indegree[v] += 1

        queue = deque(i for i in range(1, n + 1) if indegree[i] == 0)
        if len(queue) != 1:
            return False

        index = 0
        while queue:
            if len(queue) != 1:
                return False

            node = queue.popleft()
            if node != nums[index]:
                return False
            index += 1

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return index == n