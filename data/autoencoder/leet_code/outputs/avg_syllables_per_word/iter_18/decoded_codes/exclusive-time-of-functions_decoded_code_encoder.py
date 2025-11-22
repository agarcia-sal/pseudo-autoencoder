class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        exclusive_time = [0] * n
        stack = []
        for log_entry in logs:
            function_id_text, action_type, timestamp_text = log_entry.split(':')
            function_id = int(function_id_text)
            timestamp = int(timestamp_text)
            if action_type == "start":
                if stack:
                    prev_func_id, prev_timestamp = stack[-1]
                    exclusive_time[prev_func_id] += timestamp - prev_timestamp
                stack.append((function_id, timestamp))
            else:
                prev_func_id, prev_timestamp = stack.pop()
                exclusive_time[prev_func_id] += timestamp - prev_timestamp + 1
                if stack:
                    last_func_id, _ = stack[-1]
                    stack[-1] = (last_func_id, timestamp + 1)
        return exclusive_time