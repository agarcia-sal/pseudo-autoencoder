class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first_occurrences = {}
        last_occurrences = {}

        for i, ch in enumerate(s):
            if ch not in first_occurrences:
                first_occurrences[ch] = i
            last_occurrences[ch] = i

        intervals = []
        for ch in first_occurrences:
            start = first_occurrences[ch]
            end = last_occurrences[ch]
            i = start
            while i <= end:
                if first_occurrences[s[i]] < start:
                    break
                end = max(end, last_occurrences[s[i]])
                i += 1
            else:
                intervals.append((start, end))

        intervals.sort(key=lambda x: x[1])

        res = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                res.append(s[start:end + 1])
                prev_end = end

        return res