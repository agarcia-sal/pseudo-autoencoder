from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        know_secret = {0, firstPerson}
        meetings.sort(key=lambda x: x[2])
        i = 0
        while i < len(meetings):
            current_time = meetings[i][2]
            graph = defaultdict(list)
            while i < len(meetings) and meetings[i][2] == current_time:
                x, y = meetings[i][0], meetings[i][1]
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