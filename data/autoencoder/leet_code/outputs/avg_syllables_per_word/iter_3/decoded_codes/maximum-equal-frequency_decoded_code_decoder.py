from collections import Counter

class Solution:
    def maxEqualFreq(self, nums):
        count = Counter()
        freq = Counter()
        max_len = 0

        for i, num in enumerate(nums):
            prev_count = count[num]
            count[num] += 1

            if prev_count > 0:
                freq[prev_count] -= 1
                if freq[prev_count] == 0:
                    del freq[prev_count]

            freq[count[num]] += 1

            if len(freq) == 1:
                k = next(iter(freq))
                if k == 1 or freq[k] == 1:
                    max_len = i + 1
            elif len(freq) == 2:
                keys = sorted(freq)
                k1, k2 = keys[0], keys[1]
                if (k1 == 1 and freq[k1] == 1) or (k2 - k1 == 1 and freq[k2] == 1):
                    max_len = i + 1

        return max_len