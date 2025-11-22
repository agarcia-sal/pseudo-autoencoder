from collections import defaultdict

class Solution:
    def maxEqualFreq(self, nums):
        count = defaultdict(int)
        freq = defaultdict(int)
        max_len = 0

        for i, num in enumerate(nums):
            if count[num] > 0:
                freq[count[num]] -= 1
                if freq[count[num]] == 0:
                    del freq[count[num]]
            count[num] += 1
            freq[count[num]] += 1

            if len(freq) == 1:
                key = next(iter(freq))
                if key == 1 or freq[key] == 1:
                    max_len = i + 1
            elif len(freq) == 2:
                keys = list(freq.keys())
                min_k, max_k = min(keys), max(keys)
                if (freq.get(1, 0) == 1) or (max_k - min_k == 1 and freq[max_k] == 1):
                    max_len = i + 1

        return max_len