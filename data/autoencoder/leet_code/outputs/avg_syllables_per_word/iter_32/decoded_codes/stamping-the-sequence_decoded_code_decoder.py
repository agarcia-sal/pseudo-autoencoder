from collections import deque
from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        len_stamp = len(stamp)
        len_target = len(target)

        # indeg[i] counts how many characters in target from i to i+len_stamp-1 match the stamp
        indeg = [len_stamp] * (len_target - len_stamp + 1)
        # graph[pos] lists windows (indices in indeg) that contain pos-th character of target but mismatch the stamp character at that window
        graph = [[] for _ in range(len_target)]
        queue = deque()

        # Build the indeg and graph
        for i in range(len_target - len_stamp + 1):
            for j in range(len_stamp):
                c = stamp[j]
                if target[i + j] == c:
                    indeg[i] -= 1
                    if indeg[i] == 0:
                        queue.append(i)
                else:
                    graph[i + j].append(i)

        visited = [False] * len_target
        answer = []

        # BFS to simulate stamping
        while queue:
            cur = queue.popleft()
            answer.append(cur)
            for i in range(len_stamp):
                pos = cur + i
                if not visited[pos]:
                    visited[pos] = True
                    for nei in graph[pos]:
                        indeg[nei] -= 1
                        if indeg[nei] == 0:
                            queue.append(nei)

        if all(visited):
            return answer[::-1]
        else:
            return []