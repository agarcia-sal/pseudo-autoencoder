class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        intervals = []
        n = len(s)
        start = 0

        # Build initial intervals of consecutive characters
        for i in range(1, n):
            current_character = s[i]
            start_character = s[start]
            if current_character != start_character:
                intervals.append((start, i - 1, start_character))
                start = i
        intervals.append((start, n - 1, s[start]))

        def merge_intervals():
            i = 0
            while i < len(intervals) - 1:
                current_start, current_end, current_char = intervals[i]
                next_start, next_end, next_char = intervals[i + 1]
                if current_char == next_char:
                    merged_interval = (current_start, next_end, current_char)
                    intervals[i] = merged_interval
                    intervals.pop(i + 1)
                else:
                    i += 1

        results = []
        longest = max(end - start + 1 for start, end, _ in intervals)

        for char, idx in zip(queryCharacters, queryIndices):
            i = 0
            # Find the interval containing idx
            while i < len(intervals):
                current_start, current_end, current_char = intervals[i]
                if current_start <= idx <= current_end:
                    break
                i += 1

            current_start, current_end, current_char = intervals[i]

            # If idx is not at start, split left part
            if idx > current_start:
                intervals.insert(i, (current_start, idx - 1, current_char))
                i += 1  # Shift i to the right as we inserted before
                current_start = idx

            # If idx is not at end, split right part
            if idx < current_end:
                intervals.insert(i + 1, (idx + 1, current_end, current_char))
                current_end = idx

            intervals[i] = (current_start, current_end, char)

            merge_intervals()

            longest = max(end - start + 1 for start, end, _ in intervals)
            results.append(longest)

        return results