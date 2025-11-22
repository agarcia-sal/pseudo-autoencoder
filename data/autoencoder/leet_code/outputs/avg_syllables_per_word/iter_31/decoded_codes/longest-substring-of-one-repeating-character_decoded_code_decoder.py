from typing import List, Tuple


class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: List[int]
    ) -> List[int]:

        def merge_intervals() -> None:
            i = 0
            while i < len(intervals) - 1:
                first_interval_char = intervals[i][2]
                second_interval_char = intervals[i + 1][2]
                if first_interval_char == second_interval_char:
                    merged_start = intervals[i][0]
                    merged_end = intervals[i + 1][1]
                    merged_char = first_interval_char
                    intervals[i] = (merged_start, merged_end, merged_char)
                    intervals.pop(i + 1)
                else:
                    i += 1

        intervals: List[Tuple[int, int, str]] = []
        n = len(s)
        if n == 0:
            # No intervals, all queries return 0
            return [0] * len(queryCharacters)

        start = 0
        for i in range(1, n):
            current_char = s[i]
            start_char = s[start]
            if current_char != start_char:
                intervals.append((start, i - 1, start_char))
                start = i
        intervals.append((start, n - 1, s[start]))

        results = []
        longest = max((end - start + 1) for start, end, _ in intervals) if intervals else 0

        for char, idx in zip(queryCharacters, queryIndices):
            # Find interval containing idx
            i = 0
            while i < len(intervals):
                interval_start, interval_end, interval_char = intervals[i]
                if interval_start <= idx <= interval_end:
                    break
                i += 1

            interval_start, interval_end, interval_char = intervals[i]

            # Split the interval according to idx position
            # Insert new intervals as needed, making sure to avoid invalid intervals

            # Split left if idx > interval_start
            if idx > interval_start:
                # Left interval: interval_start to idx-1
                intervals.insert(i, (interval_start, idx - 1, interval_char))
                # Update current interval to start at idx
                intervals[i + 1] = (idx, interval_end, interval_char)
                i += 1  # The updated interval is now at i

            # Split right if idx < interval_end
            if idx < interval_end:
                # Right interval: idx+1 to interval_end
                intervals.insert(i + 1, (idx + 1, interval_end, interval_char))
                # Update current interval to end at idx
                intervals[i] = (interval_start, idx, interval_char)

            # Now update the interval at i to have the new char
            updated_interval_start, updated_interval_end, _ = intervals[i]
            intervals[i] = (updated_interval_start, updated_interval_end, char)

            merge_intervals()

            longest = max((end - start + 1) for start, end, _ in intervals)
            results.append(longest)

        return results