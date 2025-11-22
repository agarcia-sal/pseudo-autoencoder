from collections import Counter

def find_pairs(nums, k):
    if k < 0:
        return 0
    count = Counter(nums)
    pairs = 0
    for n in count:
        if k == 0 and count[n] > 1:
            pairs += 1
        elif k > 0 and n + k in count:
            pairs += 1
    return pairs