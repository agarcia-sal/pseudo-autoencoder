class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first, last = {}, {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        intervals = []
        for c in first:
            start, end = first[c], last[c]
            i = start
            while i <= end:
                if first[s[i]] < start:
                    break
                end = max(end, last[s[i]])
                i += 1
            if i > end:
                intervals.append((start, end))

        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                result.append(s[start:end+1])
                prev_end = end

        return result