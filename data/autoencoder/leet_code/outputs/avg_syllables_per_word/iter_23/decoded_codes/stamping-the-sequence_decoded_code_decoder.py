from collections import deque
from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        length_of_stamp = len(stamp)
        length_of_target = len(target)
        indeg = [length_of_stamp] * (length_of_target - length_of_stamp + 1)
        queue = deque()
        graph = [[] for _ in range(length_of_target)]

        for index_i in range(length_of_target - length_of_stamp + 1):
            for index_j, character_c in enumerate(stamp):
                if target[index_i + index_j] == character_c:
                    indeg[index_i] -= 1
                    if indeg[index_i] == 0:
                        queue.append(index_i)
                else:
                    graph[index_i + index_j].append(index_i)

        answer = []
        visited = [False] * length_of_target
        while queue:
            index_i = queue.popleft()
            answer.append(index_i)
            for index_j in range(length_of_stamp):
                pos = index_i + index_j
                if not visited[pos]:
                    visited[pos] = True
                    for index_k in graph[pos]:
                        indeg[index_k] -= 1
                        if indeg[index_k] == 0:
                            queue.append(index_k)

        if all(visited):
            return answer[::-1]
        else:
            return []