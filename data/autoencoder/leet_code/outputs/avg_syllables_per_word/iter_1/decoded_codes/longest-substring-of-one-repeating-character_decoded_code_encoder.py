def longest_runs_after_updates(s, queryCharacters, queryIndices):
    # Initialize intervals by splitting s into consecutive runs: (start, end, char)
    intervals = []
    start = 0
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[i - 1]:
            intervals.append([start, i - 1, s[i - 1]])
            start = i

    results = []

    def find_interval(idx):
        # Binary search to find interval containing idx
        low, high = 0, len(intervals) - 1
        while low <= high:
            mid = (low + high) // 2
            if intervals[mid][0] <= idx <= intervals[mid][1]:
                return mid
            elif idx < intervals[mid][0]:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def merge_intervals():
        merged = []
        for interval in intervals:
            if merged and merged[-1][2] == interval[2] and merged[-1][1] + 1 == interval[0]:
                merged[-1][1] = interval[1]
            else:
                merged.append(interval)
        return merged

    longest = max(end - start + 1 for start, end, _ in intervals)

    for char, idx in zip(queryCharacters, queryIndices):
        i = find_interval(idx)
        start, end, old_char = intervals[i]

        new_intervals = []

        # Left segment if idx > start
        if idx > start:
            new_intervals.append([start, idx - 1, old_char])

        # New char interval (single index if no right segment else from idx to idx)
        # We'll update the i-th interval to start at idx for now
        new_intervals.append([idx, idx, char])

        # Right segment if idx < end
        if idx < end:
            new_intervals.append([idx + 1, end, old_char])

        # Replace i-th interval with new_intervals
        intervals = intervals[:i] + new_intervals + intervals[i + 1:]

        intervals = merge_intervals()

        longest = max(end - start + 1 for start, end, _ in intervals)
        results.append(longest)

    return results