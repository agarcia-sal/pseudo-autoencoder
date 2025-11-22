from collections import Counter

class Solution:
    def maxEqualFreq(self, nums):
        count = Counter()
        freq = Counter()
        max_len = 0

        for i, num in enumerate(nums):
            old_freq = count[num]
            count[num] += 1
            new_freq = count[num]

            if old_freq > 0:
                freq[old_freq] -= 1
                if freq[old_freq] == 0:
                    del freq[old_freq]

            freq[new_freq] += 1

            if len(freq) == 1:
                key = next(iter(freq))
                if key == 1 or freq[key] == 1:
                    max_len = i + 1
            elif len(freq) == 2:
                keys = sorted(freq)
                if 1 in freq and freq[1] == 1:
                    max_len = i + 1
                elif keys[1] - keys[0] == 1 and freq[keys[1]] == 1:
                    max_len = i + 1

        return max_len