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
                            computed_hour = int(h1 + h2)
                            computed_minute = int(m1 + m2)
                            if 0 <= computed_hour < 24 and 0 <= computed_minute < 60:
                                times.append((computed_hour, computed_minute))
            return sorted(times)

        all_times = generate_times(digits)
        current_time_index = all_times.index((hour, minute))

        next_index = current_time_index + 1 if current_time_index + 1 < len(all_times) else 0
        next_hour, next_minute = all_times[next_index]

        return f"{next_hour:02d}:{next_minute:02d}"