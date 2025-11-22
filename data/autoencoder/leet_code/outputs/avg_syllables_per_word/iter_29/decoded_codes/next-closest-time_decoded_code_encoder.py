class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = set(time.replace(":", ""))
        hour = int(time[0:2])
        minute = int(time[3:5])

        def generate_times(digit_set):
            times = []
            for h1 in digit_set:
                for h2 in digit_set:
                    combined_hour = int(h1 + h2)
                    if combined_hour >= 24:
                        continue
                    for m1 in digit_set:
                        for m2 in digit_set:
                            combined_minute = int(m1 + m2)
                            if combined_minute < 60:
                                times.append((combined_hour, combined_minute))
            return sorted(times)

        all_times = generate_times(digits)
        current_time_index = all_times.index((hour, minute))

        if current_time_index + 1 < len(all_times):
            next_hour, next_minute = all_times[current_time_index + 1]
        else:
            next_hour, next_minute = all_times[0]

        return f"{next_hour:02d}:{next_minute:02d}"