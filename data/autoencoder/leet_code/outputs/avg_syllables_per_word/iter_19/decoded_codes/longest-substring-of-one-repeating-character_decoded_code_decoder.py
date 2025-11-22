from typing import List, Tuple

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        intervals: List[Tuple[int, int, str]] = []
        n = len(s)
        start = 0
        # Initialize intervals with consecutive character runs
        for i in range(1, n):
            if s[i] != s[start]:
                intervals.append((start, i - 1, s[start]))
                start = i
        intervals.append((start, n - 1, s[start]))

        def merge_intervals() -> None:
            i = 0
            while i < len(intervals) - 1:
                c1 = intervals[i][2]
                c2 = intervals[i + 1][2]
                if c1 == c2:
                    merged = (intervals[i][0], intervals[i + 1][1], c1)
                    intervals[i] = merged
                    intervals.pop(i + 1)
                else:
                    i += 1

        results = []
        longest = max(end - start + 1 for start, end, _ in intervals)

        for character, index in zip(queryCharacters, queryIndices):
            i = 0
            # Find the interval containing index
            while i < len(intervals):
                start, end, c = intervals[i]
                if start <= index <= end:
                    break
                i += 1

            # If the character at index is already the target character, no change needed
            if c == character:
                results.append(longest)
                continue

            # Split interval around index if needed
            # Left part before index
            if index > start:
                intervals.insert(i, (start, index - 1, c))
                intervals[i + 1] = (index, end, c)
                i += 1  # The current interval is now the middle one (index to end)
                start, end, c = intervals[i]

            # Right part after index
            if index < end:
                intervals.insert(i + 1, (index + 1, end, c))
                intervals[i] = (start, index, c)
                end = index  # update end of current interval

            # Update the character at the single position index to the new character
            intervals[i] = (intervals[i][0], intervals[i][1], character)

            # Merge any adjacent intervals with same characters after update
            merge_intervals()

            longest = max(end - start + 1 for start, end, _ in intervals)
            results.append(longest)

        return results