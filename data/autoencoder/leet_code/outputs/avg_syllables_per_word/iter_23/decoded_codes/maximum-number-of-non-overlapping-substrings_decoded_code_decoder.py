from typing import List, Dict

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        first: Dict[str, int] = {}
        last: Dict[str, int] = {}

        # Record first and last occurrences of each character
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        intervals = []
        for c in first:
            start = first[c]
            end = last[c]
            i = start
            # Expand the interval while checking characters inside the current interval
            while i <= end:
                if first[s[i]] < start:
                    break
                end = max(end, last[s[i]])
                i += 1
            else:
                # No break => valid interval
                intervals.append((start, end))

        # Sort intervals by their ending positions
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1  # less than any valid start
        for start, end in intervals:
            if start > prev_end:
                result.append(s[start:end+1])
                prev_end = end

        return result