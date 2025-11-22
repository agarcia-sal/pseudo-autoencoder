from collections import defaultdict, deque
from typing import List

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        tree = defaultdict(list)
        for child, parent in zip(pid, ppid):
            tree[parent].append(child)
        queue = deque([kill])
        killed_processes = []
        while queue:
            current = queue.popleft()
            killed_processes.append(current)
            for child in tree[current]:
                queue.append(child)
        return killed_processes