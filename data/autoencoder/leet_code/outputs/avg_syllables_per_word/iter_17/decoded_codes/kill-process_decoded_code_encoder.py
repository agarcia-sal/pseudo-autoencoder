from collections import defaultdict
from typing import List

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        tree = defaultdict(list)
        for child_process, parent_process in zip(pid, ppid):
            tree[parent_process].append(child_process)

        queue = [kill]
        killed_processes = []
        while queue:
            current_process = queue.pop(0)
            killed_processes.append(current_process)
            queue.extend(tree[current_process])

        return killed_processes