from collections import Counter

class Solution:
    def maxEqualFreq(self, nums):
        count = Counter()  # frequency of each num
        freq = Counter()   # frequency of frequencies
        max_len = 0

        for i, num in enumerate(nums):
            old_count = count[num]
            new_count = old_count + 1
            count[num] = new_count

            if old_count > 0:
                freq[old_count] -= 1
                if freq[old_count] == 0:
                    del freq[old_count]

            freq[new_count] += 1

            if len(freq) == 1:
                (k, v), = freq.items()
                # Either all numbers appear once or only one number has frequency k
                if k == 1 or v == 1:
                    max_len = i + 1
            elif len(freq) == 2:
                keys = sorted(freq.keys())
                k1, k2 = keys[0], keys[1]
                v1, v2 = freq[k1], freq[k2]

                if (k1 == 1 and v1 == 1) or (k2 == k1 + 1 and v2 == 1):
                    max_len = i + 1

        return max_len