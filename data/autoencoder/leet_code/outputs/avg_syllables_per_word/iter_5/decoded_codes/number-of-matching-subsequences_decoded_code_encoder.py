from collections import defaultdict, deque

class Solution:
    def numMatchingSubseq(self, s, words):
        waiting = defaultdict(deque)
        for word in words:
            it = iter(word)
            first_char = next(it, None)
            if first_char is not None:
                waiting[first_char].append(it)
        match_count = 0
        for c in s:
            current_iters = waiting[c]
            waiting[c] = deque()
            while current_iters:
                it = current_iters.popleft()
                next_char = next(it, None)
                if next_char is None:
                    match_count += 1
                else:
                    waiting[next_char].append(it)
        return match_count