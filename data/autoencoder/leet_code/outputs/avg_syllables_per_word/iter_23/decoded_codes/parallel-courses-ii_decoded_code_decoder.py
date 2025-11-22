from collections import deque, defaultdict
from typing import List, Dict

class Solution:
    def minNumberOfSemesters(self, n: int, k: int, relations: List[List[int]]) -> int:
        graph: Dict[int, List[int]] = defaultdict(list)
        in_degree: List[int] = [0] * (n + 1)

        for previous_course, next_course in relations:
            graph[previous_course].append(next_course)
            in_degree[next_course] += 1

        queue: deque[int] = deque()
        for course in range(1, n + 1):
            if in_degree[course] == 0:
                queue.append(course)

        semesters = 0
        while len(queue) > 0:
            limit = min(k, len(queue))
            for _ in range(limit):
                current_course = queue.popleft()
                for next_course in graph[current_course]:
                    in_degree[next_course] -= 1
                    if in_degree[next_course] == 0:
                        queue.append(next_course)
            semesters += 1

        return semesters