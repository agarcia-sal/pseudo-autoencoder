class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        exclusive_time_list = [0] * n
        call_stack = []

        for log_entry in logs:
            function_identifier_str, action_type, time_stamp_str = log_entry.split(':')
            function_identifier = int(function_identifier_str)
            time_stamp = int(time_stamp_str)

            if action_type == "start":
                if call_stack:
                    prev_func_id, prev_time = call_stack[-1]
                    exclusive_time_list[prev_func_id] += time_stamp - prev_time
                call_stack.append((function_identifier, time_stamp))
            else:
                prev_func_id, prev_time = call_stack.pop()
                exclusive_time_list[prev_func_id] += time_stamp - prev_time + 1
                if call_stack:
                    caller_func_id, _ = call_stack[-1]
                    call_stack[-1] = (caller_func_id, time_stamp + 1)

        return exclusive_time_list