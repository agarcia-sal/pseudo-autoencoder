from collections import Counter
from typing import List

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
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
                # Only one frequency
                key = next(iter(freq))
                if key == 1 or freq[key] == 1:
                    max_len = i + 1
            elif len(freq) == 2:
                keys = sorted(freq)
                k1, k2 = keys[0], keys[1]
                # Condition 1: freq contains 1 with exactly one element
                if (1 in freq and freq[1] == 1):
                    max_len = i + 1
                # Condition 2: max key and min key differ by 1 and max freq count is 1
                elif (k2 - k1 == 1 and freq[k2] == 1):
                    max_len = i + 1

        return max_len