from collections import Counter

class Solution:
    def maxEqualFreq(self, nums):
        count = Counter()
        freq = Counter()
        max_len = 0

        for index, num in enumerate(nums):
            prev_count = count[num]
            count[num] += 1
            curr_count = count[num]

            if prev_count > 0:
                freq[prev_count] -= 1
                if freq[prev_count] == 0:
                    del freq[prev_count]

            freq[curr_count] += 1

            if len(freq) == 1:
                key, val = next(iter(freq.items()))
                if key == 1 or val == 1:
                    max_len = index + 1
            elif len(freq) == 2:
                keys = sorted(freq.keys())
                key1, key2 = keys[0], keys[1]
                val1, val2 = freq[key1], freq[key2]
                if (key1 == 1 and val1 == 1) or (key2 - key1 == 1 and val2 == 1):
                    max_len = index + 1

        return max_len