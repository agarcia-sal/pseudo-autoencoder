class Solution:
    def maxDistToClosest(self, seats):
        max_distance = 0
        start = 0
        n = len(seats)

        while start < n and seats[start] == 0:
            start += 1

        end = n - 1
        while end >= 0 and seats[end] == 0:
            end -= 1

        if max_distance < start:
            max_distance = start

        if max_distance < n - end - 1:
            max_distance = n - end - 1

        current_distance = 0
        for i in range(start, end + 1):
            if seats[i] == 0:
                current_distance += 1
                midpoint_distance = (current_distance + 1) // 2
                if max_distance < midpoint_distance:
                    max_distance = midpoint_distance
            else:
                current_distance = 0

        return max_distance