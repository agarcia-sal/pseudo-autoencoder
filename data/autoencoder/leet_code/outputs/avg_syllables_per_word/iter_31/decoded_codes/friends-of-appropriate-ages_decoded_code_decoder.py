from typing import List

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def request_will_be_sent(age_x: int, age_y: int) -> bool:
            # Returns True if person of age_x will send friend request to person of age_y
            return not (age_y <= 0.5 * age_x + 7 or age_y > age_x or (age_y > 100 and age_x < 100))

        count = [0] * 121
        for age in ages:
            if 1 <= age <= 120:
                count[age] += 1

        total_requests = 0
        for age_x in range(1, 121):
            cx = count[age_x]
            if cx == 0:
                continue
            for age_y in range(1, 121):
                cy = count[age_y]
                if cy == 0:
                    continue
                if request_will_be_sent(age_x, age_y):
                    total_requests += cx * cy - (cx if age_x == age_y else 0)

        return total_requests