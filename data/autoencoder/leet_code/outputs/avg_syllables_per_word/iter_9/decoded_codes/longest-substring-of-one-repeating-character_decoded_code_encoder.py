class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        intervals = []
        n = len(s)
        start = 0

        for i in range(1, n):
            if s[i] != s[start]:
                intervals.append([start, i - 1, s[start]])
                start = i
        intervals.append([start, n - 1, s[start]])

        def merge_intervals():
            i = 0
            while i < len(intervals) - 1:
                if intervals[i][2] == intervals[i + 1][2]:
                    intervals[i][1] = intervals[i + 1][1]
                    intervals.pop(i + 1)
                else:
                    i += 1

        results = []
        longest = max(end - start + 1 for start, end, _ in intervals)

        for c, idx in zip(queryCharacters, queryIndices):
            i = 0
            while i < len(intervals):
                start, end, ch = intervals[i]
                if start <= idx <= end:
                    break
                i += 1

            if idx > start:
                intervals.insert(i, [start, idx - 1, ch])
                intervals[i + 1][0] = idx
                i += 1
            if idx < end:
                intervals.insert(i + 1, [idx + 1, end, ch])
                intervals[i][1] = idx

            intervals[i][2] = c

            merge_intervals()
            longest = max(end - start + 1 for start, end, _ in intervals)
            results.append(longest)

        return results