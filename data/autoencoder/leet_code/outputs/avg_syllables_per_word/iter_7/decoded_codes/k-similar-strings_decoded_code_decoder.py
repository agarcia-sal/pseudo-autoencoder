from collections import deque
from typing import Generator, Set, Tuple

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        def neighbors(s: str) -> Generator[str, None, None]:
            i = 0
            while i < len(s) and s[i] == s2[i]:
                i += 1
            for j in range(i + 1, len(s)):
                if s[j] == s2[i] and s[j] != s2[j]:
                    yield s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

        queue = deque([(s1, 0)])
        visited: Set[str] = {s1}

        while queue:
            s, swaps = queue.popleft()
            if s == s2:
                return swaps
            for neighbor in neighbors(s):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, swaps + 1))