from typing import List, Tuple

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        # intervals: List of tuples (start, end, char), representing consecutive character segments in s
        def merge_intervals():
            i = 0
            while i < len(intervals) - 1:
                start_current, end_current, char_current = intervals[i]
                start_next, end_next, char_next = intervals[i + 1]
                if char_current == char_next:
                    # Merge current and next intervals
                    intervals[i] = (start_current, end_next, char_current)
                    intervals.pop(i + 1)
                else:
                    i += 1

        n = len(s)
        intervals: List[Tuple[int, int, str]] = []
        start = 0
        # Build initial intervals from s
        for i in range(1, n):
            if s[i] != s[start]:
                intervals.append((start, i - 1, s[start]))
                start = i
        intervals.append((start, n - 1, s[start]))

        results = []
        longest = max(end - start + 1 for start, end, _ in intervals) if intervals else 0

        for char, idx in zip(queryCharacters, queryIndices):
            i = 0
            # Find the interval that contains idx
            while i < len(intervals):
                start_i, end_i, c = intervals[i]
                if start_i <= idx <= end_i:
                    break
                i += 1

            start_i, end_i, c = intervals[i]

            # If idx > start_i, split left part
            if idx > start_i:
                intervals.insert(i, (start_i, idx - 1, c))
                intervals[i + 1] = (idx, end_i, c)
                i += 1  # The modified interval is now at i

            # If idx < end_i, split right part
            if idx < end_i:
                intervals.insert(i + 1, (idx + 1, end_i, c))
                intervals[i] = (start_i if idx == start_i else intervals[i][0], idx, c)

            # Replace the char at idx with new char
            intervals[i] = (intervals[i][0], intervals[i][1], char)

            merge_intervals()

            longest = max(end - start + 1 for start, end, _ in intervals)
            results.append(longest)

        return results