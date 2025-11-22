from collections import defaultdict

class Solution:
    def killProcess(self, pid, ppid, kill):
        tree = defaultdict(list)
        for child, parent in zip(pid, ppid):
            tree[parent].append(child)
        queue = [kill]
        killed_processes = []
        while queue:
            current = queue.pop(0)
            killed_processes.append(current)
            for child in tree[current]:
                queue.append(child)
        return killed_processes