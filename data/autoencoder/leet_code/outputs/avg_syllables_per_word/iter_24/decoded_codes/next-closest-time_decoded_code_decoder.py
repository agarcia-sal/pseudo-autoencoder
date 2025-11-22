class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = set(time.replace(":", ""))
        hour = int(time[:2])
        minute = int(time[3:5])

        def generate_times(digits):
            times = []
            for h1 in digits:
                for h2 in digits:
                    for m1 in digits:
                        for m2 in digits:
                            hour_str = h1 + h2
                            minute_str = m1 + m2
                            hour_val = int(hour_str)
                            minute_val = int(minute_str)
                            if hour_val < 24 and minute_val < 60:
                                times.append((hour_val, minute_val))
            return sorted(times)

        all_times = generate_times(digits)
        current_time_index = all_times.index((hour, minute))

        if current_time_index + 1 < len(all_times):
            next_hour, next_minute = all_times[current_time_index + 1]
        else:
            next_hour, next_minute = all_times[0]

        formatted_next_hour = f"{next_hour:02d}"
        formatted_next_minute = f"{next_minute:02d}"
        formatted_time = f"{formatted_next_hour}:{formatted_next_minute}"
        return formatted_time