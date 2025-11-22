from collections import deque, defaultdict

def kill_process(pid, ppid, kill):
    tree = defaultdict(list)
    for child, parent in zip(pid, ppid):
        tree[parent].append(child)

    queue = deque([kill])
    killed = []

    while queue:
        cur = queue.popleft()
        killed.append(cur)
        queue.extend(tree[cur])

    return killed