class Solution:
    def maxNumOfSubstrings(self, s: str):
        first = {}
        last = {}

        for index, ch in enumerate(s):
            if ch not in first:
                first[ch] = index
            last[ch] = index

        intervals = []
        for ch in first:
            start = first[ch]
            end = last[ch]
            i = start
            while i <= end:
                if first[s[i]] < start:
                    break
                end = max(end, last[s[i]])
                i += 1
            else:
                intervals.append((start, end))

        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                result.append(s[start:end+1])
                prev_end = end

        return result