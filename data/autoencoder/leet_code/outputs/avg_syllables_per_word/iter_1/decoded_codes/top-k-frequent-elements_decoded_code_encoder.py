from collections import Counter

def top_k_frequent(nums, k):
    freq_map = Counter(nums)
    max_freq = max(freq_map.values())
    buckets = [[] for _ in range(max_freq + 1)]
    for num, f in freq_map.items():
        buckets[f].append(num)
    res = []
    for f in range(max_freq, 0, -1):
        if buckets[f]:
            res.extend(buckets[f])
            if len(res) >= k:
                return res[:k]
    return res