from bisect import bisect_left

def k_empty_slots(bulbs, k):
    bloom_days = []
    for day, pos in enumerate(bulbs, start=1):
        i = bisect_left(bloom_days, pos)
        if i > 0 and pos - bloom_days[i-1] - 1 == k:
            return day
        if i < len(bloom_days) and bloom_days[i] - pos - 1 == k:
            return day
        bloom_days.insert(i, pos)
    return -1