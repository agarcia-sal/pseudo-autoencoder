from collections import defaultdict, deque
from typing import List

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        tree = defaultdict(list)
        for child, parent in zip(pid, ppid):
            tree[parent].append(child)

        killed_processes = []
        queue = deque([kill])

        while queue:
            current = queue.popleft()
            killed_processes.append(current)
            queue.extend(tree[current])

        return killed_processes