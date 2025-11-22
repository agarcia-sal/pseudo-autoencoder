class Solution:
    def exclusiveTime(self, number_of_functions: int, list_of_logs: list[str]) -> list[int]:
        exclusive_time = [0] * number_of_functions
        stack = []

        for log in list_of_logs:
            function_id_str, action_str, timestamp_str = log.split(':')
            function_id = int(function_id_str)
            timestamp = int(timestamp_str)

            if action_str == "start":
                if stack:
                    prev_function_id, prev_timestamp = stack[-1]
                    exclusive_time[prev_function_id] += timestamp - prev_timestamp
                stack.append((function_id, timestamp))
            else:  # action_str == "end"
                prev_function_id, prev_timestamp = stack.pop()
                exclusive_time[prev_function_id] += timestamp - prev_timestamp + 1
                if stack:
                    last_function_id, _ = stack[-1]
                    stack[-1] = (last_function_id, timestamp + 1)

        return exclusive_time