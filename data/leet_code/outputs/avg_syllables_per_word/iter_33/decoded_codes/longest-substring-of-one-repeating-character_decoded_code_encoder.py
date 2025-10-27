from typing import List, Tuple

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        intervals: List[Tuple[int, int, str]] = []
        n = len(s)
        start = 0
        for i in range(1, n):
            if s[i] != s[start]:
                intervals.append((start, i - 1, s[start]))
                start = i
        intervals.append((start, n - 1, s[start]))

        def merge_intervals() -> None:
            i = 0
            while i < len(intervals) - 1:
                if intervals[i][2] == intervals[i + 1][2]:
                    merged = (intervals[i][0], intervals[i + 1][1], intervals[i][2])
                    intervals[i] = merged
                    intervals.pop(i + 1)
                else:
                    i += 1

        results: List[int] = []
        longest = max(end - start + 1 for start, end, _ in intervals)

        for char, idx in zip(queryCharacters, queryIndices):
            i = 0
            while i < len(intervals):
                start, end, c = intervals[i]
                if start <= idx <= end:
                    break
                i += 1

            # Split intervals as needed before modifying character
            # If idx > start, split left part
            if idx > start:
                intervals.insert(i, (start, idx - 1, c))
                intervals[i + 1] = (idx, end, c)
                i += 1  # Update i to point to the interval containing idx

            # If idx < end, split right part
            if idx < intervals[i][1]:
                start_i, end_i, c_i = intervals[i]
                intervals.insert(i + 1, (idx + 1, end_i, c_i))
                intervals[i] = (start_i, idx, c_i)

            # Update the character at idx
            start_i, end_i, _ = intervals[i]
            intervals[i] = (start_i, end_i, char)

            # Merge adjacent intervals with the same character
            merge_intervals()

            # Update longest repeating substring length
            longest = max(end - start + 1 for start, end, _ in intervals)
            results.append(longest)

        return results