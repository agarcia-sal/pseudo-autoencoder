from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        intervals = []
        for c in first:
            start = first[c]
            end = last[c]
            i = start
            # Expand the interval to include all characters that appear inside it
            # while ensuring the start indices do not go before the current start
            while i <= end:
                # If any character inside [start, end] has a first occurrence before start,
                # this interval is invalid
                if first[s[i]] < start:
                    break
                # Extend the end to cover the last occurrence of the current character
                if last[s[i]] > end:
                    end = last[s[i]]
                i += 1
            else:
                # Only add the interval if the while did not break early
                intervals.append((start, end))

        # Sort intervals by their end index to apply greedy selection of non-overlapping substrings
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                result.append(s[start:end+1])
                prev_end = end

        return result