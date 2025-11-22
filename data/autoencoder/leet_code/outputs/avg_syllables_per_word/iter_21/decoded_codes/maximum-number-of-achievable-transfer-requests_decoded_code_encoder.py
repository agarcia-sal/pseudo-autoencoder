from typing import List

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        max_requests = 0
        num_requests = len(requests)

        for mask in range(1 << num_requests):
            balance = self.create_zero_list(n)
            count = 0

            for i in range(num_requests):
                if (mask & (1 << i)) > 0:
                    from_building, to_building = requests[i]
                    balance[from_building] -= 1
                    balance[to_building] += 1
                    count += 1

            if all(b == 0 for b in balance):
                max_requests = max(max_requests, count)

        return max_requests

    def create_zero_list(self, size: int) -> List[int]:
        return [0] * size