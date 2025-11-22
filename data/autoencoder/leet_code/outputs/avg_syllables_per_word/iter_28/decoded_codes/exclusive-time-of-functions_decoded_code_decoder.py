from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exclusive_time = [0] * n
        stack = []

        for log in logs:
            function_id_str, action, timestamp_str = log.split(':')
            function_id, timestamp = int(function_id_str), int(timestamp_str)

            if action == "start":
                if stack:
                    prev_function_id, prev_timestamp = stack[-1]
                    exclusive_time[prev_function_id] += timestamp - prev_timestamp
                stack.append([function_id, timestamp])
            else:
                prev_function_id, prev_timestamp = stack.pop()
                exclusive_time[prev_function_id] += timestamp - prev_timestamp + 1
                if stack:
                    stack[-1][1] = timestamp + 1

        return exclusive_time