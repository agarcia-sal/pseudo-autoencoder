from collections import defaultdict, deque

class Solution:
    def sequenceReconstruction(self, nums, sequences):
        n = len(nums)
        graph, indegree = self.initializeGraph(n)

        for sequence in sequences:
            for index in range(len(sequence) - 1):
                u = sequence[index]
                v = sequence[index + 1]
                self.appendNeighbor(graph, u, v)
                indegree[v] += 1

        queue = self.initializeQueue(indegree)
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

    def initializeGraph(self, n):
        graph = defaultdict(list)
        indegree = [0] * (n + 1)
        return graph, indegree

    def appendNeighbor(self, graph, u, v):
        graph[u].append(v)

    def initializeQueue(self, indegree):
        queue = deque()
        for i in range(1, len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        return queue