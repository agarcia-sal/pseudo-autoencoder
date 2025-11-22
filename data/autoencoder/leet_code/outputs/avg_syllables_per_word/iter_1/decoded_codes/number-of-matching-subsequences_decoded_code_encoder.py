from collections import defaultdict, deque

def num_matching_subseq(s, words):
    waiting = defaultdict(deque)
    for c in s:
        waiting[c] = deque()

    for word in words:
        it = iter(word)
        first = next(it)
        if first in waiting:
            waiting[first].append(it)

    match_count = 0
    for c in s:
        current = waiting[c]
        waiting[c] = deque()
        while current:
            it = current.popleft()
            nxt = next(it, None)
            if nxt is None:
                match_count += 1
            elif nxt in waiting:
                waiting[nxt].append(it)
    return match_count