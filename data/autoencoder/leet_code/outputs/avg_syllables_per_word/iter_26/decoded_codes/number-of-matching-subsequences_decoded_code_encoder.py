from collections import deque, defaultdict
from typing import List, Iterator, Optional


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting: dict[str, deque[Iterator[str]]] = defaultdict(deque)

        # Initialize waiting with empty queues for all unique chars in s
        for c in set(s):
            waiting[c] = deque()

        # Populate waiting with iterators of words grouped by their first letter
        for word in words:
            it = iter(word)
            first_letter: Optional[str] = next(it, None)
            if first_letter is not None and first_letter in waiting:
                waiting[first_letter].append(it)

        match_count = 0

        # Process the string s, advancing iterators where the current character matches
        for c in s:
            if c in waiting:
                current_iterators = waiting[c]
                waiting[c] = deque()
                while current_iterators:
                    it = current_iterators.popleft()
                    next_char = next(it, None)
                    if next_char is None:
                        match_count += 1
                    elif next_char in waiting:
                        waiting[next_char].append(it)

        return match_count