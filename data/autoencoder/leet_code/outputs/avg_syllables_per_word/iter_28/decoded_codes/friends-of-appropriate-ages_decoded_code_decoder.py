from typing import List

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def request_will_be_sent(age_x: int, age_y: int) -> bool:
            return not (
                age_y <= age_x // 2 + 7
                or age_y > age_x
                or (age_y > 100 and age_x < 100)
            )

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
                    if age_x == age_y:
                        total_requests += count[age_x] * (count[age_y] - 1)
                    else:
                        total_requests += count[age_x] * count[age_y]

        return total_requests