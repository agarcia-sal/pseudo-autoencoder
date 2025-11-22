from collections import Counter

class Solution:
    def maxEqualFreq(self, nums):
        count = Counter()
        freq = Counter()
        max_len = 0

        for i, num in enumerate(nums):
            old_freq = count[num]
            count[num] = old_freq + 1
            new_freq = count[num]

            if old_freq > 0:
                freq[old_freq] -= 1
                if freq[old_freq] == 0:
                    del freq[old_freq]

            freq[new_freq] += 1

            if len(freq) == 1:
                # Either all numbers have the same frequency,
                # or frequency is 1 for all
                key = next(iter(freq))
                if key == 1 or freq[key] == 1:
                    max_len = i + 1
            elif len(freq) == 2:
                keys = list(freq.keys())
                k1, k2 = min(keys), max(keys)
                # Check if one frequency is 1 and occurs once,
                # or frequencies differ by one and the higher frequency occurs once
                if (freq.get(1, 0) == 1 and freq[1] == 1) or (k2 - k1 == 1 and freq[k2] == 1):
                    max_len = i + 1

        return max_len