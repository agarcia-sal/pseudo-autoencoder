class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        # intervals: list of tuples (start, end, char), representing consecutive intervals of same chars in s
        intervals = []
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
                start_first, end_first, char_first = intervals[i]
                start_second, end_second, char_second = intervals[i + 1]
                if char_first == char_second:
                    intervals[i] = (start_first, end_second, char_first)
                    intervals.pop(i + 1)
                else:
                    i += 1

        results = []
        longest = max(end - start + 1 for start, end, _ in intervals)

        # Process queries
        for char, idx in zip(queryCharacters, queryIndices):
            # Binary search for the interval containing idx
            left, right = 0, len(intervals) - 1
            i = -1
            while left <= right:
                mid = (left + right) // 2
                start_i, end_i, c_i = intervals[mid]
                if start_i <= idx <= end_i:
                    i = mid
                    break
                elif idx < start_i:
                    right = mid - 1
                else:
                    left = mid + 1
            if i == -1:
                # idx is out of range - edge case
                raise IndexError("queryIndices contains index out of string range")

            start_i, end_i, c_i = intervals[i]

            # Split intervals if necessary
            new_intervals = []

            # If idx > start, interval before idx
            if idx > start_i:
                new_intervals.append((start_i, idx - 1, c_i))

            # The position idx itself - to be updated to new char later
            new_intervals.append((idx, idx, char))

            # If idx < end, interval after idx
            if idx < end_i:
                new_intervals.append((idx + 1, end_i, c_i))

            # Replace intervals[i] with new_intervals
            intervals = intervals[:i] + new_intervals + intervals[i + 1:]

            # Merge adjacent intervals with same char
            merge_intervals()

            longest = max(end - start + 1 for start, end, _ in intervals)
            results.append(longest)

        return results