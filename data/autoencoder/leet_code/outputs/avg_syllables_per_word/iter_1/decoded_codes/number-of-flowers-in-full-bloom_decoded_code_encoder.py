from bisect import bisect_left, bisect_right

def count_flowers(flowers, people):
    starts = sorted(s for s, e in flowers)
    ends = sorted(e for s, e in flowers)
    res = []
    for p in people:
        started = bisect_right(starts, p)
        ended = bisect_left(ends, p)
        res.append(started - ended)
    return res