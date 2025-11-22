from collections import defaultdict, deque
from typing import List, Dict

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        know_secret = {0, firstPerson}
        meetings.sort(key=lambda x: x[2])
        i = 0
        length = len(meetings)
        while i < length:
            current_time = meetings[i][2]
            graph: Dict[int, List[int]] = defaultdict(list)
            while i < length and meetings[i][2] == current_time:
                x = meetings[i][0]
                y = meetings[i][1]
                graph[x].append(y)
                graph[y].append(x)
                i += 1
            queue = deque(p for p in know_secret if p in graph)
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