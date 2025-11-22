from collections import Counter

class Solution:
    def maxEqualFreq(self, nums) -> int:
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
                # Key can be '1', or the sole value can be 1
                (key, val), = freq.items()
                if key == 1 or val == 1:
                    max_len = index + 1
            elif len(freq) == 2:
                keys = sorted(freq.keys())
                v1, v2 = freq[keys[0]], freq[keys[1]]

                # Condition 1: freq contains 1 and freq[1] == 1
                if keys[0] == 1 and v1 == 1:
                    max_len = index + 1
                # Condition 2: difference between keys == 1 and freq of higher key == 1
                elif keys[1] - keys[0] == 1 and v2 == 1:
                    max_len = index + 1

        return max_len