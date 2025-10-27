from collections import Counter

class Solution:
    def maxEqualFreq(self, nums):
        count = Counter()  # count of each number
        freq = Counter()   # freq of each count
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
                (f, c), = freq.items()
                if f == 1 or c == 1:
                    max_len = i + 1
            elif len(freq) == 2:
                keys = sorted(freq.keys())
                f1, f2 = keys[0], keys[1]
                c1, c2 = freq[f1], freq[f2]
                # Check conditions:
                # 1) freq has key 1 with count 1
                # 2) difference between keys is 1 and the higher freq occurs once
                if (f1 == 1 and c1 == 1) or (f2 - f1 == 1 and c2 == 1):
                    max_len = i + 1

        return max_len