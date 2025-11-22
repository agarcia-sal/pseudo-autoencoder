from collections import deque, defaultdict

class Solution:
    def numMatchingSubseq(self, s, words):
        waiting = defaultdict(deque)
        for c in set(s):
            waiting[c] = deque()
        for word in words:
            it = iter(word)
            first_letter = next(it, None)
            if first_letter in waiting:
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
                    else:
                        if next_char in waiting:
                            waiting[next_char].append(it)
        return match_count