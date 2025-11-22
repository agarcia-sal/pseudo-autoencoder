from typing import List, Tuple

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        def merge_intervals() -> None:
            i = 0
            while i < len(intervals) - 1:
                current_start, current_end, current_char = intervals[i]
                next_start, next_end, next_char = intervals[i+1]
                if current_char == next_char:
                    intervals[i] = (current_start, next_end, current_char)
                    intervals.pop(i+1)
                else:
                    i += 1

        intervals: List[Tuple[int, int, str]] = []
        n = len(s)
        start = 0

        for i in range(1, n):
            if s[i] != s[start]:
                intervals.append((start, i - 1, s[start]))
                start = i
        intervals.append((start, n - 1, s[start]))

        results = []
        # Helper to calculate the longest interval length
        def longest_interval_len() -> int:
            if not intervals:
                return 0
            return max(end - start + 1 for start, end, _ in intervals)

        longest = longest_interval_len()

        for char, idx in zip(queryCharacters, queryIndices):
            # Find the interval that contains idx
            i = 0
            while i < len(intervals):
                interval_start, interval_end, interval_char = intervals[i]
                if interval_start <= idx <= interval_end:
                    break
                i += 1
            else:
                # idx not found within any interval, which theoretically shouldn't happen
                # but handle gracefully
                i = -1

            if i == -1:
                # idx not found, no update possible, append current longest and continue
                results.append(longest)
                continue

            interval_start, interval_end, interval_char = intervals[i]

            # Split the original interval if idx is not at the boundary
            # Insert intervals for left part if it exists
            inserts = []

            if idx > interval_start:
                inserts.append((interval_start, idx - 1, interval_char))

            # Middle interval at idx with the new character
            inserts.append((idx, idx, char))

            # Right part if exists
            if idx < interval_end:
                inserts.append((idx + 1, interval_end, interval_char))

            # Replace the original interval with inserts
            intervals.pop(i)
            for j, new_interval in enumerate(inserts):
                intervals.insert(i + j, new_interval)

            # Merge intervals after update
            merge_intervals()

            # Update longest
            longest = longest_interval_len()
            results.append(longest)

        return results