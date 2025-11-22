from collections import Counter

class Solution:
    def maxEqualFreq(self, nums):
        count = Counter()
        freq = Counter()
        max_len = 0

        for i, num in enumerate(nums):
            prev_count = count[num]
            if prev_count > 0:
                freq[prev_count] -= 1
                if freq[prev_count] == 0:
                    del freq[prev_count]

            count[num] += 1
            curr_count = count[num]
            freq[curr_count] += 1

            if len(freq) == 1:
                (f, c), = freq.items()
                if f == 1 or c == 1:
                    max_len = i + 1
            elif len(freq) == 2:
                keys = list(freq.keys())
                k1, k2 = min(keys), max(keys)
                if (k1 == 1 and freq[k1] == 1) or (k2 - k1 == 1 and freq[k2] == 1):
                    max_len = i + 1

        return max_len