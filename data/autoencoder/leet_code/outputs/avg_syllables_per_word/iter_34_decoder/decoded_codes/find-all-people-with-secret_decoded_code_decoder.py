from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        know_secret = {0, firstPerson}
        meetings.sort(key=lambda x: x[2])
        i = 0
        while i < len(meetings):
            current_time = meetings[i][2]
            graph = defaultdict(list)
            # Build the graph for all meetings at current_time
            while i < len(meetings) and meetings[i][2] == current_time:
                x, y, _ = meetings[i]
                graph[x].append(y)
                graph[y].append(x)
                i += 1
            # BFS to spread the secret among connected people at current_time
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
        return list(know_secret)