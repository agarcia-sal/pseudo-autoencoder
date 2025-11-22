class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        intervals = []
        n = len(s)
        start = 0
        for i in range(1, n):
            current_char = s[i]
            start_char = s[start]
            if current_char != start_char:
                intervals.append((start, i - 1, start_char))
                start = i
        intervals.append((start, n - 1, s[start]))

        def merge_intervals() -> None:
            i = 0
            while i < len(intervals) - 1:
                start_current, end_current, char_current = intervals[i]
                start_next, end_next, char_next = intervals[i + 1]
                if char_current == char_next:
                    intervals[i] = (start_current, end_next, char_current)
                    intervals.pop(i + 1)
                else:
                    i += 1

        results = []
        longest = 0
        for start_i, end_i, char_i in intervals:
            length = end_i - start_i + 1
            if length > longest:
                longest = length

        for char, idx in zip(queryCharacters, queryIndices):
            i = 0
            while i < len(intervals):
                start_i, end_i, c = intervals[i]
                if start_i <= idx <= end_i:
                    break
                i += 1

            # Split interval if idx not at boundaries
            if idx > start_i:
                left_tuple = (start_i, idx - 1, c)
                intervals.insert(i, left_tuple)
                right_tuple = (idx, end_i, c)
                intervals[i + 1] = right_tuple
                i += 1
                start_i = idx

            if idx < end_i:
                middle_tuple = (start_i, idx, c)
                intervals.insert(i + 1, (idx + 1, end_i, c))
                intervals[i] = middle_tuple
                end_i = idx

            intervals[i] = (start_i, end_i, char)

            merge_intervals()

            longest = 0
            for start_j, end_j, char_j in intervals:
                length = end_j - start_j + 1
                if length > longest:
                    longest = length
            results.append(longest)

        return results