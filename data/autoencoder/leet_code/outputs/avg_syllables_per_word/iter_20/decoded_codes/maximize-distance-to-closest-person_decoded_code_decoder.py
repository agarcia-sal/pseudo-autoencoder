from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_distance = 0
        n = len(seats)
        start = 0

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
                dist = (current_distance + 1) // 2
                if max_distance < dist:
                    max_distance = dist
            else:
                current_distance = 0

        return max_distance