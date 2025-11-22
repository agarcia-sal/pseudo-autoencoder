from collections import defaultdict, deque
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(deque)
        for word in words:
            it = iter(word)
            first_letter = next(it, None)
            if first_letter in waiting or first_letter in s:
                waiting[first_letter].append(it)

        match_count = 0
        for c in s:
            if c in waiting:
                current_iterators = waiting[c]
                waiting[c] = deque()
                while current_iterators:
                    it = current_iterators.popleft()
                    next_char = next(it, None)
                    if next_char is None:
                        match_count += 1
                    elif next_char in waiting or next_char in s:
                        waiting[next_char].append(it)
        return match_count