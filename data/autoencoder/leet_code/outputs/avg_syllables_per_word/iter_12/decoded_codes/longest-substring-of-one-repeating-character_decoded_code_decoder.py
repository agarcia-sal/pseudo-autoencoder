from typing import List, Tuple

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        # intervals: List of tuples (start, end, char)
        intervals: List[Tuple[int, int, str]] = []
        n = len(s)
        start = 0
        for i in range(1, n):
            if s[i] != s[start]:
                intervals.append((start, i - 1, s[start]))
                start = i
        intervals.append((start, n - 1, s[start]))

        def merge_intervals():
            i = 0
            while i < len(intervals) - 1:
                start_1, end_1, char_1 = intervals[i]
                start_2, end_2, char_2 = intervals[i + 1]
                if char_1 == char_2:
                    new_start = start_1
                    new_end = end_2
                    merged_char = char_1
                    intervals[i] = (new_start, new_end, merged_char)
                    intervals.pop(i + 1)
                else:
                    i += 1

        results = []
        longest = max(end - start + 1 for start, end, _ in intervals) if intervals else 0

        for char, idx in zip(queryCharacters, queryIndices):
            i = 0
            while i < len(intervals):
                start_i, end_i, c = intervals[i]
                if start_i <= idx <= end_i:
                    break
                i += 1

            start_i, end_i, c = intervals[i]

            if idx > start_i:
                # Insert left interval
                intervals.insert(i, (start_i, idx - 1, c))
                # Update i to point to right interval
                intervals[i + 1] = (idx, end_i, c)
                i += 1  # Now i points to interval that contains idx

            if idx < end_i:
                # Insert right interval after current
                intervals.insert(i + 1, (idx + 1, end_i, c))
                # Update current interval's end to idx
                intervals[i] = (start_i if idx == start_i else intervals[i][0], idx, c)

            # Replace the character at idx with new char
            intervals[i] = (intervals[i][0], intervals[i][1], char)

            merge_intervals()

            longest = max(end - start + 1 for start, end, _ in intervals)
            results.append(longest)

        return results