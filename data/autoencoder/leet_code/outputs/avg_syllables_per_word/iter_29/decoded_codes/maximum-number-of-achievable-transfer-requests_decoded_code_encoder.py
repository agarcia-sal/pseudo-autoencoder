from typing import List

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        maximum_number_of_requests = 0
        total_number_of_requests = len(requests)

        for mask in range(1 << total_number_of_requests):
            balance_list = [0] * n
            current_request_count = 0

            for index in range(total_number_of_requests):
                if mask & (1 << index):
                    from_building = requests[index][0]
                    to_building = requests[index][1]
                    balance_list[from_building] -= 1
                    balance_list[to_building] += 1
                    current_request_count += 1

            if all(balance == 0 for balance in balance_list):
                if current_request_count > maximum_number_of_requests:
                    maximum_number_of_requests = current_request_count

        return maximum_number_of_requests