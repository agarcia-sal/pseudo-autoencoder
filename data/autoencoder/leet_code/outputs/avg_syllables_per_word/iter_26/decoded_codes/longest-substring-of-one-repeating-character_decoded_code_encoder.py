class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        intervals = []
        n = len(s)
        start = 0
        # Build initial intervals of consecutive equal characters
        for i in range(1, n):
            if s[i] != s[start]:
                intervals.append((start, i - 1, s[start]))
                start = i
        intervals.append((start, n - 1, s[start]))

        def merge_intervals():
            i = 0
            while i < len(intervals) - 1:
                if intervals[i][2] == intervals[i + 1][2]:
                    merged = (intervals[i][0], intervals[i + 1][1], intervals[i][2])
                    intervals[i] = merged
                    intervals.pop(i + 1)
                else:
                    i += 1

        results = []
        longest = max(e - s + 1 for s, e, _ in intervals)

        for char, idx in zip(queryCharacters, queryIndices):
            i = 0
            while i < len(intervals):
                start, end, c = intervals[i]
                if start <= idx <= end:
                    break
                i += 1

            # Split interval if needed before the idx
            if idx > start:
                intervals.insert(i, (start, idx - 1, c))
                intervals[i + 1] = (idx, end, c)
                i += 1  # Adjust i since we inserted before it

            # Split interval if needed after the idx
            if idx < intervals[i][1]:
                start_i, end_i, c_i = intervals[i]
                intervals.insert(i + 1, (idx + 1, end_i, c_i))
                intervals[i] = (start_i, idx, c_i)

            # Replace the character at position idx
            intervals[i] = (intervals[i][0], intervals[i][1], char)

            merge_intervals()

            longest = max(e - s + 1 for s, e, _ in intervals)
            results.append(longest)

        return results