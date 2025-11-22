from collections import Counter

def check_frequency(nums, k):
    freq = Counter(nums)
    max_freq = max(freq.values())
    return (len(nums) // k) >= max_freq