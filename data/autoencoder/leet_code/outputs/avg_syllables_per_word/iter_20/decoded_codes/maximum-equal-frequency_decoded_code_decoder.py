from collections import Counter

class Solution:
    def maxEqualFreq(self, nums: list[int]) -> int:
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
                key = next(iter(freq))
                if key == 1 or freq[key] == 1:
                    max_len = i + 1
            elif len(freq) == 2:
                keys = sorted(freq)
                min_key, max_key = keys[0], keys[1]
                # Case 1: one of the frequencies is 1 and freq[1] == 1
                if (min_key == 1 and freq[min_key] == 1) or \
                   (max_key - min_key == 1 and freq[max_key] == 1):
                    max_len = i + 1

        return max_len