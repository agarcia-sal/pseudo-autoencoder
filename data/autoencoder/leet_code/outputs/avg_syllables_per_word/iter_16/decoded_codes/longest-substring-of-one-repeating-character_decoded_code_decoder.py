class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
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
                current_char = intervals[i][2]
                next_char = intervals[i + 1][2]
                if current_char == next_char:
                    new_start = intervals[i][0]
                    new_end = intervals[i + 1][1]
                    intervals[i] = (new_start, new_end, current_char)
                    intervals.pop(i + 1)
                else:
                    i += 1

        results = []
        longest = max(end - start + 1 for start, end, _ in intervals) if intervals else 0

        for ch, idx in zip(queryCharacters, queryIndices):
            i = 0
            while i < len(intervals):
                curr_start, curr_end, curr_char = intervals[i]
                if curr_start <= idx <= curr_end:
                    break
                i += 1

            # intervals[i] covers idx
            curr_start, curr_end, curr_char = intervals[i]

            # split intervals as needed
            new_intervals = []

            if idx > curr_start:
                new_intervals.append((curr_start, idx - 1, curr_char))

            new_intervals.append((idx, idx, ch))

            if idx < curr_end:
                new_intervals.append((idx + 1, curr_end, curr_char))

            # Replace intervals[i] with new intervals
            intervals.pop(i)
            for interval in reversed(new_intervals):
                intervals.insert(i, interval)

            merge_intervals()

            longest = max(end - start + 1 for start, end, _ in intervals) if intervals else 0
            results.append(longest)

        return results