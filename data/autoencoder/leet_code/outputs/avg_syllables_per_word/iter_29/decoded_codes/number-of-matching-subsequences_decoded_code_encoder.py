from collections import defaultdict, deque
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(deque)
        for word in words:
            it = iter(word)
            first_char = next(it, None)
            if first_char is not None and first_char in s:
                waiting[first_char].append(it)
        match_count = 0
        for c in s:
            if c in waiting:
                current_iters = waiting[c]
                waiting[c] = deque()
                while current_iters:
                    it = current_iters.popleft()
                    next_char = next(it, None)
                    if next_char is None:
                        match_count += 1
                    elif next_char in s:
                        waiting[next_char].append(it)
        return match_count