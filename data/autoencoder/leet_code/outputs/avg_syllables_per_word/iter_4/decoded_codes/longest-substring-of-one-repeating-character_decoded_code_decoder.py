class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: [int]) -> [int]:
        def merge_intervals():
            i = 0
            while i < len(intervals) - 1:
                if intervals[i][2] == intervals[i + 1][2]:
                    intervals[i] = (intervals[i][0], intervals[i + 1][1], intervals[i][2])
                    intervals.pop(i + 1)
                else:
                    i += 1

        intervals = []
        n = len(s)
        start = 0
        for i in range(1, n):
            if s[i] != s[start]:
                intervals.append((start, i - 1, s[start]))
                start = i
        intervals.append((start, n - 1, s[start]))

        results = []
        longest = max(end - start + 1 for start, end, _ in intervals)

        for char, idx in zip(queryCharacters, queryIndices):
            i = 0
            while i < len(intervals):
                start, end, c = intervals[i]
                if start <= idx <= end:
                    break
                i += 1

            start, end, c = intervals[i]

            if idx > start:
                intervals.insert(i, (start, idx - 1, c))
                i += 1
                intervals[i] = (idx, end, c)
            if idx < end:
                intervals.insert(i + 1, (idx + 1, end, c))
                intervals[i] = (start, idx, c)

            intervals[i] = (intervals[i][0], intervals[i][1], char)

            merge_intervals()

            longest = max(end - start + 1 for start, end, _ in intervals)
            results.append(longest)

        return results