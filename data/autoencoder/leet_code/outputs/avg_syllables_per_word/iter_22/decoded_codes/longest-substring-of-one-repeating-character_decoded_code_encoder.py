from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        intervals = []
        n = len(s)
        start = 0

        # Build initial intervals of consecutive repeating characters
        for i in range(1, n):
            if s[i] != s[start]:
                intervals.append((start, i - 1, s[start]))
                start = i
        intervals.append((start, n - 1, s[start]))

        def merge_intervals():
            i = 0
            while i < len(intervals) - 1:
                # If adjacent intervals have the same character, merge them
                if intervals[i][2] == intervals[i + 1][2]:
                    # Merge current and next intervals
                    new_interval = (intervals[i][0], intervals[i + 1][1], intervals[i][2])
                    intervals[i] = new_interval
                    del intervals[i + 1]
                else:
                    i += 1

        results = []
        longest = max(end - start + 1 for start, end, _ in intervals) if intervals else 0

        for c, idx in zip(queryCharacters, queryIndices):
            i = 0
            while i < len(intervals):
                start, end, ch = intervals[i]
                if start <= idx <= end:
                    break
                i += 1

            # Split intervals as necessary around idx
            # Left part
            if idx > start:
                intervals.insert(i, (start, idx - 1, ch))
                i += 1
                intervals[i] = (idx, end, ch)
                start = idx  # Update start for the current interval

            # Right part
            if idx < intervals[i][1]:
                intervals.insert(i + 1, (idx + 1, intervals[i][1], intervals[i][2]))
                intervals[i] = (intervals[i][0], idx, intervals[i][2])

            # Replace the character at position idx
            intervals[i] = (intervals[i][0], intervals[i][1], c)

            merge_intervals()

            longest = max(end - start + 1 for start, end, _ in intervals)
            results.append(longest)

        return results