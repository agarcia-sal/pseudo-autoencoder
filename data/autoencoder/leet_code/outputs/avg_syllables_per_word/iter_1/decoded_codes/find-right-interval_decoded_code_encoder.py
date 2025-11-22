from bisect import bisect_left

def find_right_intervals(intervals):
    sort_starts = sorted((s, i) for i, (s, _) in enumerate(intervals))
    res = []
    for _, e in intervals:
        pos = bisect_left(sort_starts, (e,))
        res.append(sort_starts[pos][1] if pos < len(sort_starts) else -1)
    return res