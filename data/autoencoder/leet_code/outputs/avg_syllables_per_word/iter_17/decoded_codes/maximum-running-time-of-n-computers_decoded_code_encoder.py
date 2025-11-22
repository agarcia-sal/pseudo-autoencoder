class Solution:
    def maxRunTime(self, number_of_computers: int, battery_capacities: list[int]) -> int:
        def canRunFor(proposed_time: int) -> bool:
            total_runtime = 0
            for capacity in battery_capacities:
                total_runtime += min(capacity, proposed_time)
            return total_runtime >= proposed_time * number_of_computers

        left, right = 0, sum(battery_capacities) // number_of_computers

        while left < right:
            mid = (left + right + 1) // 2
            if canRunFor(mid):
                left = mid
            else:
                right = mid - 1

        return left