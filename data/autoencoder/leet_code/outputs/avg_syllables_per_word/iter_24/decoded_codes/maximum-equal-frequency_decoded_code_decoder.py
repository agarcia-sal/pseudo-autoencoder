from collections import Counter

class Solution:
    def maxEqualFreq(self, nums):
        count = Counter()
        freq = Counter()
        max_len = 0

        for i, num in enumerate(nums):
            prev_freq = count[num]
            count[num] += 1
            curr_freq = count[num]

            if prev_freq > 0:
                freq[prev_freq] -= 1
                if freq[prev_freq] == 0:
                    del freq[prev_freq]
            freq[curr_freq] += 1

            if len(freq) == 1:
                (f, c), = freq.items()
                if f == 1 or c == 1:
                    max_len = i + 1
            elif len(freq) == 2:
                (f1, c1), (f2, c2) = freq.items()
                max_f, min_f = max(f1, f2), min(f1, f2)
                max_c = c1 if f1 == max_f else c2
                min_c = c1 if f1 == min_f else c2

                if (min_f == 1 and min_c == 1) or (max_f - min_f == 1 and max_c == 1):
                    max_len = i + 1

        return max_len