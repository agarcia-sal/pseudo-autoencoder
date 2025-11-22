from typing import List, Tuple

class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = set(time.replace(":", ""))
        hour, minute = map(int, time.split(":"))

        def generate_times(digits: set) -> List[Tuple[int, int]]:
            times = []
            for h1 in digits:
                for h2 in digits:
                    for m1 in digits:
                        for m2 in digits:
                            h = int(h1 + h2)
                            m = int(m1 + m2)
                            if h < 24 and m < 60:
                                times.append((h, m))
            times.sort()
            return times

        all_times = generate_times(digits)
        current_time_index = all_times.index((hour, minute))
        if current_time_index + 1 < len(all_times):
            next_hour, next_minute = all_times[current_time_index + 1]
        else:
            next_hour, next_minute = all_times[0]

        return f"{next_hour:02d}:{next_minute:02d}"