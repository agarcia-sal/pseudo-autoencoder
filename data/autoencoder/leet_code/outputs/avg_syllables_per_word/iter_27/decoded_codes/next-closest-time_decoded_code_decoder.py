from typing import List, Tuple

class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = set(time.replace(":", ""))
        hour = int(time[0:2])
        minute = int(time[3:5])

        def generate_times(digits: set) -> List[Tuple[int, int]]:
            times = []
            for h1 in digits:
                for h2 in digits:
                    for m1 in digits:
                        for m2 in digits:
                            combined_hour = int(h1 + h2)
                            combined_minute = int(m1 + m2)
                            if combined_hour < 24 and combined_minute < 60:
                                times.append((combined_hour, combined_minute))
            return sorted(times)

        all_times = generate_times(digits)
        current_time = (hour, minute)

        # Find index of current_time in all_times
        # all_times is sorted and may have duplicates? (No duplicates because digits set used)
        # Just use index. If not found, fallback to first time (but should be present)
        try:
            current_time_index = all_times.index(current_time)
        except ValueError:
            # In case input time is invalid or not in generated times, return earliest time
            next_hour, next_minute = all_times[0]
            return f"{next_hour:02d}:{next_minute:02d}"

        next_index = current_time_index + 1
        if next_index < len(all_times):
            next_hour, next_minute = all_times[next_index]
        else:
            next_hour, next_minute = all_times[0]

        return f"{next_hour:02d}:{next_minute:02d}"