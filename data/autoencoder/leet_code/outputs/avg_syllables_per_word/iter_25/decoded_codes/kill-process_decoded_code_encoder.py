from collections import defaultdict
from typing import List

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        tree = defaultdict(list)
        for child, parent in zip(pid, ppid):
            tree[parent].append(child)
        queue = [kill]
        killed_processes = []
        while queue:
            current = queue.pop(0)
            killed_processes.append(current)
            queue.extend(tree[current])
        return killed_processes