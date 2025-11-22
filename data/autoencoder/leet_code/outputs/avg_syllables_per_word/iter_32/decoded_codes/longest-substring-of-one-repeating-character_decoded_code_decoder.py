from typing import List, Tuple

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        intervals: List[Tuple[int, int, str]] = []
        n = len(s)

        # Initialize intervals list by grouping consecutive same characters
        start = 0
        for i in range(1, n):
            if s[i] != s[start]:
                intervals.append((start, i - 1, s[start]))
                start = i
        intervals.append((start, n - 1, s[start]))

        def merge_intervals():
            i = 0
            while i < len(intervals) - 1:
                curr_start, curr_end, curr_char = intervals[i]
                next_start, next_end, next_char = intervals[i + 1]
                if curr_char == next_char:
                    # Merge intervals[i] and intervals[i+1]
                    intervals[i] = (curr_start, next_end, curr_char)
                    intervals.pop(i + 1)
                else:
                    i += 1

        results: List[int] = []
        # Compute initial longest run
        longest = max((end - start + 1) for start, end, _ in intervals) if intervals else 0

        for char, idx in zip(queryCharacters, queryIndices):
            # Find the interval containing idx
            i = 0
            while i < len(intervals):
                start, end, c = intervals[i]
                if start <= idx <= end:
                    break
                i += 1

            start, end, c = intervals[i]

            # Split interval into up to three parts:
            # Left (start to idx-1), Middle (idx), Right (idx+1 to end)
            new_intervals = []

            # Left part, if any
            if idx > start:
                new_intervals.append((start, idx - 1, c))

            # The changed position
            new_intervals.append((idx, idx, char))

            # Right part, if any
            if idx < end:
                new_intervals.append((idx + 1, end, c))

            # Replace intervals[i] with new_intervals
            intervals = intervals[:i] + new_intervals + intervals[i + 1:]

            merge_intervals()

            longest = max((end - start + 1) for start, end, _ in intervals) if intervals else 0
            results.append(longest)

        return results