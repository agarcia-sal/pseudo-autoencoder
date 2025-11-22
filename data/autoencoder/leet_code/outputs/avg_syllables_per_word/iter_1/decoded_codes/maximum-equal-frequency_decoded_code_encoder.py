from collections import Counter

def max_equal_freq(nums):
    count = Counter()
    freq = Counter()
    max_len = 0

    for i, num in enumerate(nums):
        if count[num] > 0:
            freq[count[num]] -= 1
            if freq[count[num]] == 0:
                del freq[count[num]]
        count[num] += 1
        freq[count[num]] += 1

        if (len(freq) == 1 and (1 in freq or list(freq.values()) == [1])) or \
           (len(freq) == 2 and ((freq.get(1,0) == 1) or ((max(freq) - min(freq) == 1) and freq[max(freq)] == 1))):
            max_len = i + 1

    return max_len