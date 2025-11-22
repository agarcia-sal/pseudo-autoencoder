from typing import List

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def request_will_be_sent(age_x: int, age_y: int) -> bool:
            if age_y <= 0.5 * age_x + 7:
                return False
            if age_y > age_x:
                return False
            if age_y > 100 and age_x < 100:
                return False
            return True

        count = [0] * 121
        for age in ages:
            if 1 <= age <= 120:
                count[age] += 1

        total_requests = 0
        for age_x in range(1, 121):
            if count[age_x] == 0:
                continue
            for age_y in range(1, 121):
                if count[age_y] == 0:
                    continue
                if request_will_be_sent(age_x, age_y):
                    requests = count[age_x] * count[age_y]
                    if age_x == age_y:
                        requests -= count[age_x]
                    total_requests += requests

        return total_requests