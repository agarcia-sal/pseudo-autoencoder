from typing import List, Tuple

class Solution:
    def maximumRequests(self, n: int, requests: List[Tuple[int, int]]) -> int:
        max_requests = 0
        num_requests = len(requests)

        for mask in range(1 << num_requests):
            balance = [0] * n
            count = 0

            for i in range(num_requests):
                if (mask >> i) & 1:
                    from_building, to_building = requests[i]
                    balance[from_building] -= 1
                    balance[to_building] += 1
                    count += 1

            if all(b == 0 for b in balance) and count > max_requests:
                max_requests = count

        return max_requests