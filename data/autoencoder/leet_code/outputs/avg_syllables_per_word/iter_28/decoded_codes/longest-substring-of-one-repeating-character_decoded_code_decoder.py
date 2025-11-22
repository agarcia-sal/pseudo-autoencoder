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
                start_i, end_i, char_i = intervals[i]
                start_next, end_next, char_next = intervals[i + 1]
                if char_i == char_next:
                    intervals[i] = (start_i, end_next, char_i)
                    intervals.pop(i + 1)
                else:
                    i += 1

        results = []
        longest = max((end - start + 1) for start, end, _ in intervals)

        for char, idx in zip(queryCharacters, queryIndices):
            i = 0
            while i < len(intervals):
                start_interval, end_interval, char_interval = intervals[i]
                if start_interval <= idx <= end_interval:
                    break
                i += 1

            if idx > start_interval:
                left_interval = (start_interval, idx - 1, char_interval)
                intervals.insert(i, left_interval)
                intervals[i + 1] = (idx, end_interval, char_interval)
                i += 1

            if idx < end_interval:
                right_interval = (idx + 1, end_interval, char_interval)
                intervals.insert(i + 1, right_interval)
                intervals[i] = (start_interval if idx == start_interval else intervals[i][0], idx, char_interval)

            intervals[i] = (intervals[i][0], intervals[i][1], char)

            merge_intervals()

            longest = max((end - start + 1) for start, end, _ in intervals)
            results.append(longest)

        return results