from collections import deque
from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        length_of_stamp = len(stamp)
        length_of_target = len(target)

        indeg_list = [length_of_stamp] * (length_of_target - length_of_stamp + 1)
        queue_structure = deque()
        graph_list = [[] for _ in range(length_of_target)]

        for index_i in range(length_of_target - length_of_stamp + 1):
            for index_j in range(length_of_stamp):
                character_c = stamp[index_j]
                if target[index_i + index_j] == character_c:
                    indeg_list[index_i] -= 1
                    if indeg_list[index_i] == 0:
                        queue_structure.append(index_i)
                else:
                    graph_list[index_i + index_j].append(index_i)

        answer_list = []
        visited_list = [False] * length_of_target

        while queue_structure:
            index_i = queue_structure.popleft()
            answer_list.append(index_i)
            for index_j in range(length_of_stamp):
                pos = index_i + index_j
                if not visited_list[pos]:
                    visited_list[pos] = True
                    for index_k in graph_list[pos]:
                        indeg_list[index_k] -= 1
                        if indeg_list[index_k] == 0:
                            queue_structure.append(index_k)

        if all(visited_list):
            return answer_list[::-1]
        return []