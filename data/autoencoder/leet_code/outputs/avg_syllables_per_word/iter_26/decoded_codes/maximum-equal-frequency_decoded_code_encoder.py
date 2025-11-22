from collections import Counter

class Solution:
    def maxEqualFreq(self, nums: list[int]) -> int:
        count = Counter()  # number -> frequency
        freq = Counter()   # frequency -> count of numbers with that frequency
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
                (f, c), = freq.items()
                # Either frequency is 1 or there's only one number with that frequency
                if f == 1 or c == 1:
                    max_len = i + 1
            elif len(freq) == 2:
                keys = sorted(freq.keys())
                f1, f2 = keys[0], keys[1]
                c1, c2 = freq[f1], freq[f2]

                # Condition 1: frequency 1 exists once
                if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
                    max_len = i + 1
                # Condition 2: frequencies differ by 1 and the higher frequency count is 1
                elif f2 - f1 == 1 and (c2 == 1 or c1 == 1):
                    max_len = i + 1

        return max_len