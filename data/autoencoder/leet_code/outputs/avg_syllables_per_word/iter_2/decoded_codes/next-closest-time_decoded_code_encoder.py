class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = set(time.replace(":", ""))
        hour, minute = map(int, time.split(":"))

        def generate_times(digits):
            times = []
            for h1 in digits:
                for h2 in digits:
                    for m1 in digits:
                        for m2 in digits:
                            hour_val = int(h1 + h2)
                            minute_val = int(m1 + m2)
                            if hour_val < 24 and minute_val < 60:
                                times.append((hour_val, minute_val))
            return sorted(times)

        all_times = generate_times(digits)
        current_time_index = all_times.index((hour, minute))

        if current_time_index + 1 < len(all_times):
            next_hour, next_minute = all_times[current_time_index + 1]
        else:
            next_hour, next_minute = all_times[0]

        return f"{next_hour:02d}:{next_minute:02d}"