from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        know_secret = {0, firstPerson}
        self.sort_meetings_by_time(meetings)

        i = 0
        length = len(meetings)
        while i < length:
            current_time = meetings[i][2]

            graph, i = self.create_graph_for_current_time(meetings, current_time, i)

            self.spread_secret_bfs(graph, know_secret)

        return list(know_secret)

    def sort_meetings_by_time(self, meetings: List[List[int]]) -> None:
        meetings.sort(key=lambda x: x[2])

    def create_graph_for_current_time(self, meetings: List[List[int]], current_time: int, start_index: int):
        graph = defaultdict(list)
        index = start_index
        length = len(meetings)
        while index < length and meetings[index][2] == current_time:
            x = meetings[index][0]
            y = meetings[index][1]

            graph[x].append(y)
            graph[y].append(x)

            index += 1

        return graph, index

    def spread_secret_bfs(self, graph: dict, know_secret: set) -> None:
        queue = deque(person for person in know_secret if person in graph)
        visited = set()

        while queue:
            person = queue.popleft()
            if person in visited:
                continue
            visited.add(person)
            know_secret.add(person)
            for neighbor in graph[person]:
                if neighbor not in visited:
                    queue.append(neighbor)