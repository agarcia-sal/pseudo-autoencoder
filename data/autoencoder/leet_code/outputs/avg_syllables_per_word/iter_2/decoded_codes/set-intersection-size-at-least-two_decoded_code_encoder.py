class Solution:
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x: (x[1], -x[0]))
        first = intervals[0][1] - 1
        second = intervals[0][1]
        count = 2
        for start, end in intervals[1:]:
            if start > second:
                first = end - 1
                second = end
                count += 2
            elif start > first:
                first = second
                second = end
                count += 1
        return count