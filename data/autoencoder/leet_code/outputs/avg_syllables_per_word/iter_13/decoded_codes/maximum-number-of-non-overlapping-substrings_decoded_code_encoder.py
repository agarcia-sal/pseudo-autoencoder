class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}

        # Record first and last occurrence of each character
        for index, c in enumerate(s):
            if c not in first:
                first[c] = index
            last[c] = index

        intervals = []
        for c in first:
            start = first[c]
            end = last[c]
            i = start
            # Expand the interval to include all characters whose first occurrences are not before start
            while i <= end:
                if first[s[i]] < start:
                    break
                end = max(end, last[s[i]])
                i += 1
            else:
                # If the loop didn't break, add the valid interval
                intervals.append((start, end))

        # Sort intervals based on end index
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                result.append(s[start:end + 1])
                prev_end = end

        return result