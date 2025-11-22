from collections import deque, defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        waiting = {c: deque() for c in set(s)}

        for word in words:
            it = iter(word)
            first_letter = next(it, None)
            if first_letter is not None and first_letter in waiting:
                waiting[first_letter].append(it)

        match_count = 0

        for c in s:
            if c in waiting:
                old_queue = waiting[c]
                waiting[c] = deque()
                while old_queue:
                    it = old_queue.popleft()
                    next_char = next(it, None)
                    if next_char is None:
                        match_count += 1
                    elif next_char in waiting:
                        waiting[next_char].append(it)

        return match_count