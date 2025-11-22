from collections import defaultdict, deque

class Solution:
    def killProcess(self, pid, ppid, kill):
        tree = defaultdict(list)
        for child, parent in zip(pid, ppid):
            tree[parent].append(child)
        queue = deque([kill])
        killed_processes = []
        while queue:
            current = queue.popleft()
            killed_processes.append(current)
            queue.extend(tree[current])
        return killed_processes