from typing import List, Tuple

class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = set(time.replace(":", ""))
        hour = int(time[:2])
        minute = int(time[3:5])

        def generate_times(digits: set) -> List[Tuple[int, int]]:
            times = []
            for h1 in digits:
                for h2 in digits:
                    for m1 in digits:
                        for m2 in digits:
                            hour_value = int(h1 + h2)
                            minute_value = int(m1 + m2)
                            if 0 <= hour_value < 24 and 0 <= minute_value < 60:
                                times.append((hour_value, minute_value))
            return sorted(times)

        all_times = generate_times(digits)
        current_time = (hour, minute)
        current_time_index = all_times.index(current_time)

        if current_time_index + 1 < len(all_times):
            next_hour, next_minute = all_times[current_time_index + 1]
        else:
            next_hour, next_minute = all_times[0]

        formatted_hour = f"{next_hour:02d}"
        formatted_minute = f"{next_minute:02d}"
        formatted_time = f"{formatted_hour}:{formatted_minute}"

        return formatted_time