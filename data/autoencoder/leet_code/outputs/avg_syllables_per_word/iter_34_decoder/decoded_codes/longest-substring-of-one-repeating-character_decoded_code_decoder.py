class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        intervals = []
        n = len(s)
        start = 0
        # Build initial intervals representing consecutive equal characters
        for i in range(1, n):
            if s[i] != s[start]:
                intervals.append((start, i - 1, s[start]))
                start = i
        intervals.append((start, n - 1, s[start]))

        def merge_intervals():
            i = 0
            while i < len(intervals) - 1:
                start_i, end_i, c_i = intervals[i]
                start_next, end_next, c_next = intervals[i + 1]
                if c_i == c_next:
                    # merge intervals i and i+1
                    intervals[i] = (start_i, end_next, c_i)
                    intervals.pop(i + 1)
                else:
                    i += 1

        results = []
        longest = max(end - start + 1 for start, end, _ in intervals) if intervals else 0

        for char, idx in zip(queryCharacters, queryIndices):
            i = 0
            # Find the interval containing idx
            while i < len(intervals):
                start, end, c = intervals[i]
                if start <= idx <= end:
                    break
                i += 1

            start, end, c = intervals[i]
            new_intervals = []

            # If idx is not at the start, insert the left part interval
            if idx > start:
                new_intervals.append((start, idx - 1, c))

            # Insert the updated character interval at idx
            new_intervals.append((idx, idx, char))

            # If idx is not at the end, insert the right part interval
            if idx < end:
                new_intervals.append((idx + 1, end, c))

            # Replace the original interval with new intervals
            intervals[i:i + 1] = new_intervals

            # Merge adjacent intervals with same characters
            merge_intervals()

            longest = max(end - start + 1 for start, end, _ in intervals)
            results.append(longest)

        return results