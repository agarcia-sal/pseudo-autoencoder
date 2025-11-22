from collections import deque, defaultdict

def min_number_of_semesters(n, relations, k):
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)

    for prev, nxt in relations:
        graph[prev].append(nxt)
        in_degree[nxt] += 1

    queue = deque([course for course in range(1, n + 1) if in_degree[course] == 0])
    semesters = 0

    while queue:
        # Take up to k courses from the queue
        size = min(k, len(queue))
        for _ in range(size):
            course = queue.popleft()
            for nxt in graph[course]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    queue.append(nxt)
        semesters += 1

    return semesters