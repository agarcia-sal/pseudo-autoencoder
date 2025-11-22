from collections import deque
from typing import Generator

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        def neighbors(s: str) -> Generator[str, None, None]:
            i = 0
            # Find first index where s and s2 differ
            while i < len(s) and s[i] == s2[i]:
                i += 1
            if i == len(s):
                return  # no neighbors if s == s2
            for j in range(i + 1, len(s)):
                # Swap s[i] with s[j] if it helps make s closer to s2
                if s[j] == s2[i] and s[j] != s2[j]:
                    # Construct the neighbor string with characters at i and j swapped
                    yield s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

        queue = deque([(s1, 0)])
        visited = {s1}

        while queue:
            s, swaps = queue.popleft()
            if s == s2:
                return swaps
            for neighbor in neighbors(s):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, swaps + 1))