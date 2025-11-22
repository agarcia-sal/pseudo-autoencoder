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
                            composed_hour = int(h1 + h2)
                            composed_minute = int(m1 + m2)
                            if 0 <= composed_hour < 24 and 0 <= composed_minute < 60:
                                times.append((composed_hour, composed_minute))
            times.sort()
            return times

        all_times = generate_times(digits)
        current_time_index = 0
        for i, (h, m) in enumerate(all_times):
            if h == hour and m == minute:
                current_time_index = i
                break

        if current_time_index + 1 < len(all_times):
            next_hour, next_minute = all_times[current_time_index + 1]
        else:
            next_hour, next_minute = all_times[0]

        return f"{next_hour:02d}:{next_minute:02d}"