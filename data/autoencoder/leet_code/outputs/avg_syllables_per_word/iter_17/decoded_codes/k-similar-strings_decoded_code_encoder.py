from collections import deque

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        def neighbors(s):
            i = 0
            # Find first index where s and s2 differ
            while i < len(s) and s[i] == s2[i]:
                i += 1
            for j in range(i + 1, len(s)):
                # Look for a character to swap to reduce difference
                if s[j] == s2[i] and s[j] != s2[j]:
                    # Swap characters at positions i and j
                    swapped = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                    yield swapped

        queue = deque([(s1, 0)])
        visited = {s1}

        while queue:
            s, swaps = queue.popleft()
            if s == s2:
                return swaps
            for nei in neighbors(s):
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, swaps + 1))