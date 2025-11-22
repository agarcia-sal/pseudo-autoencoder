class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        intervals = []
        n = len(s)
        start = 0
        # Build initial intervals of consecutive identical characters
        for i in range(1, n):
            if s[i] != s[start]:
                intervals.append((start, i - 1, s[start]))
                start = i
        intervals.append((start, n - 1, s[start]))

        def merge_intervals():
            i = 0
            while i < len(intervals) - 1:
                if intervals[i][2] == intervals[i + 1][2]:
                    merged = (intervals[i][0], intervals[i + 1][1], intervals[i][2])
                    intervals[i] = merged
                    intervals.pop(i + 1)
                else:
                    i += 1

        results = []
        # Initial longest repeating substring length
        longest = max(end - start + 1 for start, end, _ in intervals) if intervals else 0

        for c, index in zip(queryCharacters, queryIndices):
            i = 0
            # Find the interval containing index
            while i < len(intervals):
                start, end, ch = intervals[i]
                if start <= index <= end:
                    break
                i += 1
            else:
                # Defensive: index should always be found in intervals
                # but if not, skip this query
                results.append(longest)
                continue

            start, end, ch = intervals[i]

            # Modify intervals to reflect the character replacement at index
            # If index splits interval on the left side
            if index > start:
                intervals.insert(i, (start, index - 1, ch))
                i += 1
            # If index splits interval on the right side
            if index < end:
                intervals.insert(i + 1, (index + 1, end, ch))
            # Update the changed position interval with new character
            intervals[i] = (intervals[i][0], intervals[i][1], c)

            # Merge consecutive intervals with the same character
            merge_intervals()

            longest = max(end - start + 1 for start, end, _ in intervals) if intervals else 0
            results.append(longest)

        return results