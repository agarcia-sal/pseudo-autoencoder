class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        intervals = []
        n = len(s)
        start = 0

        # Build initial intervals from string s
        for i in range(1, n):
            if s[i] != s[start]:
                intervals.append((start, i - 1, s[start]))
                start = i
        intervals.append((start, n - 1, s[start]))

        def merge_intervals():
            i = 0
            while i < len(intervals) - 1:
                # Merge adjacent intervals if their chars are equal
                if intervals[i][2] == intervals[i + 1][2]:
                    merged = (intervals[i][0], intervals[i + 1][1], intervals[i][2])
                    intervals[i] = merged
                    intervals.pop(i + 1)
                else:
                    i += 1

        results = []
        longest = max(end - start + 1 for start, end, _ in intervals)

        for char, idx in zip(queryCharacters, queryIndices):
            # Find the interval that contains idx
            i = 0
            while i < len(intervals):
                start, end, c = intervals[i]
                if start <= idx <= end:
                    break
                i += 1

            # Split the interval if needed
            if idx > start:
                intervals.insert(i, (start, idx - 1, c))
                intervals[i + 1] = (idx, end, c)

            if idx < end:
                intervals.insert(i + 1, (idx + 1, end, c))
                intervals[i] = (start, idx, c)

            # Update the character at idx to the new char
            intervals[i] = (intervals[i][0], intervals[i][1], char)

            merge_intervals()

            longest = max(end - start + 1 for start, end, _ in intervals)
            results.append(longest)

        return results