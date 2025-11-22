class Solution:
    def exclusiveTime(self, n, logs):
        exclusive_time = [0] * n
        stack = []

        for log in logs:
            function_id_str, action, timestamp_str = log.split(':')
            function_id = int(function_id_str)
            timestamp = int(timestamp_str)

            if action == "start":
                if stack:
                    prev_function_id, prev_timestamp = stack[-1]
                    exclusive_time[prev_function_id] += timestamp - prev_timestamp
                stack.append((function_id, timestamp))
            else:
                prev_function_id, prev_timestamp = stack.pop()
                exclusive_time[prev_function_id] += timestamp - prev_timestamp + 1
                if stack:
                    top_function_id, _ = stack[-1]
                    stack[-1] = (top_function_id, timestamp + 1)

        return exclusive_time