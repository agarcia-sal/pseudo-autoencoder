class Solution:
    def numFriendRequests(self, ages):
        def request_will_be_sent(age_x, age_y):
            return not (age_y <= age_x // 2 + 7 or age_y > age_x or (age_y > 100 and age_x < 100))

        count = [0] * 121
        for age in ages:
            count[age] += 1

        total_requests = 0
        for age_x in range(1, 121):
            for age_y in range(1, 121):
                if request_will_be_sent(age_x, age_y):
                    total_requests += count[age_x] * (count[age_y] - (1 if age_x == age_y else 0))
        return total_requests