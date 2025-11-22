from collections import deque, defaultdict

def sequenceReconstruction(nums, sequences):
    n = len(nums)
    graph = defaultdict(list)
    indegree = [0] * (n + 1)

    for seq in sequences:
        for i in range(len(seq) - 1):
            u, v = seq[i], seq[i + 1]
            graph[u].append(v)
            indegree[v] += 1

    queue = deque([i for i in range(1, n + 1) if indegree[i] == 0])
    if len(queue) != 1:
        return False

    index = 0
    while queue:
        if len(queue) != 1:
            return False
        node = queue.popleft()
        if node != nums[index]:
            return False
        index += 1
        for neigh in graph[node]:
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                queue.append(neigh)

    return index == n