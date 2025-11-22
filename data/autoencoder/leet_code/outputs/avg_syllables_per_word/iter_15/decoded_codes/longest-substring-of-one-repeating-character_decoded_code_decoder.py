from typing import List, Tuple

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        def merge_intervals() -> None:
            i = 0
            while i < len(intervals) - 1:
                start1, end1, char1 = intervals[i]
                start2, end2, char2 = intervals[i + 1]
                if char1 == char2:
                    intervals[i] = (start1, end2, char1)
                    intervals.pop(i + 1)
                else:
                    i += 1

        n = len(s)
        intervals: List[Tuple[int, int, str]] = []
        start = 0
        for i in range(1, n):
            if s[i] != s[start]:
                intervals.append((start, i - 1, s[start]))
                start = i
        intervals.append((start, n - 1, s[start]))

        results: List[int] = []
        longest = max(end - start + 1 for start, end, _ in intervals) if intervals else 0

        for char, idx in zip(queryCharacters, queryIndices):
            # Find the interval containing idx
            i = 0
            while i < len(intervals):
                start_i, end_i, char_i = intervals[i]
                if start_i <= idx <= end_i:
                    break
                i += 1

            start_i, end_i, char_i = intervals[i]

            # Split interval if idx is inside it (not at boundary)
            if idx > start_i:
                intervals.insert(i, (start_i, idx - 1, char_i))
                intervals[i + 1] = (idx, end_i, char_i)
                i += 1
                start_i, end_i, char_i = intervals[i]
            if idx < end_i:
                intervals.insert(i + 1, (idx + 1, end_i, char_i))
                intervals[i] = (start_i, idx, char_i)
                start_i, end_i, char_i = intervals[i]

            # Replace character at idx
            intervals[i] = (start_i, end_i, char)

            merge_intervals()

            longest = max(end - start + 1 for start, end, _ in intervals)
            results.append(longest)

        return results