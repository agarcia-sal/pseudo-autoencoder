from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque([c for c in range(numCourses) if indegree[c] == 0])

        while queue:
            current_course = queue.popleft()
            numCourses -= 1

            for next_course in graph[current_course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return numCourses == 0