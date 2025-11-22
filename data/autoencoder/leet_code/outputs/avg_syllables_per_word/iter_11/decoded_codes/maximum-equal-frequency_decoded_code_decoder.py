from collections import defaultdict

class Solution:
    def maxEqualFreq(self, nums):
        count = defaultdict(int)
        freq = defaultdict(int)
        max_len = 0

        for i, num in enumerate(nums):
            count[num] += 1

            if count[num] > 1:
                freq[count[num] - 1] -= 1
                if freq[count[num] - 1] == 0:
                    del freq[count[num] - 1]

            freq[count[num]] += 1

            if len(freq) == 1:
                key = next(iter(freq))
                if key == 1 or freq[key] == 1:
                    max_len = i + 1
            elif len(freq) == 2:
                keys = sorted(freq)
                if (1 in freq and freq[1] == 1) or (keys[1] - keys[0] == 1 and freq[keys[1]] == 1):
                    max_len = i + 1

        return max_len