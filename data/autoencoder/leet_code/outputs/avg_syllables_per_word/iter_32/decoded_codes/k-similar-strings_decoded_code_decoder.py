from collections import deque
from typing import Generator, Set, Tuple

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        # Generate all neighbors by swapping to move s closer to s2
        def neighbors(s: str) -> Generator[str, None, None]:
            i = 0
            # Find first index where s and s2 differ
            while i < len(s) and s[i] == s2[i]:
                i += 1
            if i == len(s):
                return  # s == s2, no neighbors needed
            for j in range(i + 1, len(s)):
                # If swapping s[i] with s[j] moves the character at j to its correct position in s2
                # and s[j] != s2[j] to avoid swapping characters already in correct place
                if s[j] == s2[i] and s[j] != s2[j]:
                    # Swap characters at i and j to generate neighbor
                    ns = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                    yield ns

        queue: deque[Tuple[str, int]] = deque([(s1, 0)])
        visited: Set[str] = {s1}

        while queue:
            s, swaps = queue.popleft()
            if s == s2:
                return swaps
            for nei in neighbors(s):
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, swaps + 1))