class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        intervals = []
        n = len(s)
        start = 0

        # Build initial intervals of consecutive characters
        for i in range(1, n):
            if s[i] != s[start]:
                intervals.append((start, i - 1, s[start]))
                start = i
        intervals.append((start, n - 1, s[start]))

        def merge_intervals():
            i = 0
            while i < len(intervals) - 1:
                start_i, end_i, char_i = intervals[i]
                start_next, end_next, char_next = intervals[i + 1]
                if char_i == char_next:
                    intervals[i] = (start_i, end_next, char_i)
                    intervals.pop(i + 1)
                else:
                    i += 1

        results = []
        longest = 0
        # Calculate initial longest interval length
        for start, end, _ in intervals:
            length = end - start + 1
            if length > longest:
                longest = length

        for char, idx in zip(queryCharacters, queryIndices):
            i = 0
            # Find interval containing idx
            while i < len(intervals):
                start_i, end_i, char_i = intervals[i]
                if start_i <= idx <= end_i:
                    break
                i += 1

            start_i, end_i, char_i = intervals[i]

            # Split interval around idx if needed before changing the character
            if idx > start_i:
                intervals.insert(i, (start_i, idx - 1, char_i))
                intervals[i + 1] = (idx, end_i, char_i)
                i += 1
                start_i, end_i = idx, end_i
            if idx < end_i:
                intervals.insert(i + 1, (idx + 1, end_i, char_i))
                intervals[i] = (start_i, idx, char_i)
                end_i = idx

            # Update character at idx
            intervals[i] = (intervals[i][0], intervals[i][1], char)

            merge_intervals()

            longest = 0
            for start_m, end_m, _ in intervals:
                length = end_m - start_m + 1
                if length > longest:
                    longest = length

            results.append(longest)

        return results