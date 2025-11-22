from collections import Counter

class Solution:
    def maxEqualFreq(self, nums):
        count = Counter()  # count of each number's frequency
        freq = Counter()   # count of frequencies of frequencies
        max_len = 0

        for i, num in enumerate(nums):
            old_count = count[num]
            count[num] += 1
            new_count = count[num]

            if old_count > 0:
                freq[old_count] -= 1
                if freq[old_count] == 0:
                    del freq[old_count]
            freq[new_count] += 1

            if len(freq) == 1:
                k = next(iter(freq))
                # either frequency is 1 or only one element occurs once (freq[k] == 1)
                if k == 1 or freq[k] == 1:
                    max_len = i + 1
            elif len(freq) == 2:
                keys = sorted(freq.keys())
                k1, k2 = keys[0], keys[1]
                # Either freq 1 occurs once or max freq and min freq differ by 1 and max freq count is 1
                if (freq.get(1, 0) == 1 and freq[k2] * k2 + freq[k1] * k1 == i + 1) or \
                   (k2 - k1 == 1 and freq[k2] == 1):
                    max_len = i + 1

        return max_len