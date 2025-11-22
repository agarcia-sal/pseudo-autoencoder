class Solution:
    def maxDistToClosest(self, seats):
        n = len(seats)
        max_distance = 0

        start = 0
        while start < n and seats[start] == 0:
            start += 1

        end = n - 1
        while end >= 0 and seats[end] == 0:
            end -= 1

        max_distance = max(start, max_distance)
        max_distance = max(max_distance, n - end - 1)

        current_distance = 0
        for i in range(start, end + 1):
            if seats[i] == 0:
                current_distance += 1
                candidate_distance = (current_distance + 1) // 2
                max_distance = max(max_distance, candidate_distance)
            else:
                current_distance = 0

        return max_distance