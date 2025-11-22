from collections import Counter

class Solution:
    def maxEqualFreq(self, nums):
        count = Counter()
        freq = Counter()
        max_len = 0

        for i, num in enumerate(nums):
            prev_count = count[num]
            count[num] += 1
            curr_count = count[num]

            if prev_count > 0:
                freq[prev_count] -= 1
                if freq[prev_count] == 0:
                    del freq[prev_count]

            freq[curr_count] += 1

            if len(freq) == 1:
                (key, val), = freq.items()
                if key == 1 or val == 1:
                    max_len = i + 1
            elif len(freq) == 2:
                keys = list(freq.keys())
                vals = list(freq.values())
                if (1 in freq and freq[1] == 1) or (max(keys) - min(keys) == 1 and freq[max(keys)] == 1):
                    max_len = i + 1

        return max_len