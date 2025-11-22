from collections import defaultdict
from typing import List

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        count = defaultdict(int)  # element -> count
        freq = defaultdict(int)   # count -> frequency of counts
        max_len = 0

        for i, num in enumerate(nums):
            prev_count = count[num]
            count[num] += 1
            curr_count = count[num]

            # Decrement frequency of previous count if greater than zero
            if prev_count > 0:
                freq[prev_count] -= 1
                if freq[prev_count] == 0:
                    del freq[prev_count]

            # Increment frequency of current count
            freq[curr_count] += 1

            if len(freq) == 1:
                key = next(iter(freq))
                # Either all counts are 1, or only one number has that frequency
                if key == 1 or freq[key] == 1:
                    max_len = i + 1
            elif len(freq) == 2:
                keys = sorted(freq)
                # Check if one freq is 1 and freq[1] == 1 or difference between keys is 1 and max freq count is 1
                if (1 in freq and freq[1] == 1) or \
                        (keys[1] - keys[0] == 1 and freq[keys[1]] == 1):
                    max_len = i + 1

        return max_len