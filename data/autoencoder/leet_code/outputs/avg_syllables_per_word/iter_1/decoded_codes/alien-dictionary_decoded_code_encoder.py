from collections import defaultdict, deque

def alienOrder(words):
    graph = defaultdict(set)
    indegree = defaultdict(int)
    all_chars = set(''.join(words))

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        found = False
        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                found = True
                break
        if not found and len(w1) > len(w2):
            return ""

    queue = deque([c for c in all_chars if indegree[c] == 0])
    result = []

    while queue:
        c = queue.popleft()
        result.append(c)
        for n in graph[c]:
            indegree[n] -= 1
            if indegree[n] == 0:
                queue.append(n)

    if len(result) != len(all_chars):
        return ""

    return ''.join(result)