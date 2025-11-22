from typing import List, Tuple

class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: List[int]
    ) -> List[int]:

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
                current_start, current_end, current_char = intervals[i]
                next_start, next_end, next_char = intervals[i + 1]
                if current_char == next_char:
                    intervals[i] = (current_start, next_end, current_char)
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

            start, end, c = intervals[i]

            # Split intervals if needed
            if idx > start:
                intervals.insert(i, (start, idx - 1, c))
                intervals[i + 1] = (idx, end, c)
                i += 1
                start, end, c = intervals[i]

            if idx < end:
                intervals.insert(i + 1, (idx + 1, end, c))
                intervals[i] = (start, idx, c)

            # Set the character at idx
            intervals[i] = (intervals[i][0], intervals[i][1], char)

            merge_intervals()

            longest = max(end - start + 1 for start, end, _ in intervals)
            results.append(longest)

        return results