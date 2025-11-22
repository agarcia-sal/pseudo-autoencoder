from typing import List, Tuple

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        # Each interval is represented as a tuple: (start, end, character)
        intervals: List[Tuple[int, int, str]] = []
        n = len(s)
        start = 0

        # Build initial intervals from s
        for i in range(1, n):
            if s[i] != s[start]:
                intervals.append((start, i - 1, s[start]))
                start = i
        intervals.append((start, n - 1, s[start]))

        def merge_intervals():
            i = 0
            while i < len(intervals) - 1:
                cur_start, cur_end, cur_char = intervals[i]
                next_start, next_end, next_char = intervals[i+1]
                if cur_char == next_char:
                    # Merge intervals[i] and intervals[i+1]
                    intervals[i] = (cur_start, next_end, cur_char)
                    intervals.pop(i+1)
                else:
                    i += 1

        results = []
        longest = max(end - start + 1 for start, end, _ in intervals)

        for char, idx in zip(queryCharacters, queryIndices):
            # Find the interval containing idx
            i = 0
            while i < len(intervals):
                start_i, end_i, c = intervals[i]
                if start_i <= idx <= end_i:
                    break
                i += 1

            start_i, end_i, c = intervals[i]

            # Split interval if needed before idx
            if idx > start_i:
                intervals.insert(i, (start_i, idx - 1, c))
                intervals[i + 1] = (idx, end_i, c)
                i += 1
                start_i, end_i, c = intervals[i]

            # Split interval if needed after idx
            if idx < end_i:
                intervals.insert(i + 1, (idx + 1, end_i, c))
                intervals[i] = (start_i, idx, c)
                start_i, end_i, c = intervals[i]

            # Update the character at idx
            intervals[i] = (start_i, end_i, char)

            merge_intervals()

            longest = max(end - start + 1 for start, end, _ in intervals)
            results.append(longest)

        return results