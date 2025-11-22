from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_distance = 0
        start = 0
        n = len(seats)

        # Count zeros from the start
        while start < n and seats[start] == 0:
            start += 1

        end = n - 1
        # Count zeros from the end
        while end >= 0 and seats[end] == 0:
            end -= 1

        # Distance from leading zeros
        if max_distance < start:
            max_distance = start

        # Distance from trailing zeros
        trailing_zeros = n - end - 1
        if max_distance < trailing_zeros:
            max_distance = trailing_zeros

        current_distance = 0
        # Check zeros between first and last occupied seats
        for i in range(start, end + 1):
            if seats[i] == 0:
                current_distance += 1
                # max distance is half of the consecutive zeros (rounded up)
                dist = (current_distance + 1) // 2
                if max_distance < dist:
                    max_distance = dist
            else:
                current_distance = 0

        return max_distance