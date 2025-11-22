from collections import deque, defaultdict

def findAllPeople(n, meetings, firstPerson):
    meetings.sort(key=lambda x: x[2])
    know_secret = {0, firstPerson}
    i = 0
    while i < len(meetings):
        t = meetings[i][2]
        graph = defaultdict(list)
        # Build graph for all meetings at time t
        while i < len(meetings) and meetings[i][2] == t:
            x, y, _ = meetings[i]
            graph[x].append(y)
            graph[y].append(x)
            i += 1
        queue = deque([p for p in know_secret if p in graph])
        visited = set()
        while queue:
            p = queue.popleft()
            if p in visited:
                continue
            visited.add(p)
            know_secret.add(p)
            for n in graph[p]:
                if n not in visited:
                    queue.append(n)
    return list(know_secret)