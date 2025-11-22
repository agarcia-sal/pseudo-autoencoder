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
                start_first, end_first, char_first = intervals[i]
                start_second, end_second, char_second = intervals[i + 1]
                if char_first == char_second:
                    intervals[i] = (start_first, end_second, char_first)
                    intervals.pop(i + 1)
                else:
                    i += 1

        results: List[int] = []
        longest = max(end - start + 1 for start, end, _ in intervals) if intervals else 0

        for char, idx in zip(queryCharacters, queryIndices):
            i = 0
            while i < len(intervals):
                start_current, end_current, char_current = intervals[i]
                if start_current <= idx <= end_current:
                    break
                i += 1

            start_current, end_current, char_current = intervals[i]

            # Split intervals around idx if necessary
            # Insert left part if idx > start_current
            if idx > start_current:
                intervals.insert(i, (start_current, idx - 1, char_current))
                i += 1
                intervals[i] = (idx, end_current, char_current)
                start_current, end_current, char_current = intervals[i]

            # Insert right part if idx < end_current
            if idx < end_current:
                intervals.insert(i + 1, (idx + 1, end_current, char_current))
                intervals[i] = (start_current, idx, char_current)
                # now intervals[i] is left, intervals[i+1] is right
            # Update the character at idx position
            intervals[i] = (intervals[i][0], intervals[i][1], char)

            merge_intervals()

            longest = max(end - start + 1 for start, end, _ in intervals) if intervals else 0
            results.append(longest)

        return results