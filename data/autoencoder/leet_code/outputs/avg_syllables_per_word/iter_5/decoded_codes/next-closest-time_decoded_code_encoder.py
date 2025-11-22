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
                            hh = int(h1 + h2)
                            mm = int(m1 + m2)
                            if hh < 24 and mm < 60:
                                times.append((hh, mm))
            return sorted(times)

        all_times = generate_times(digits)
        current = (hour, minute)
        idx = all_times.index(current)

        next_idx = idx + 1 if idx + 1 < len(all_times) else 0
        next_hour, next_minute = all_times[next_idx]
        return f"{next_hour:02d}:{next_minute:02d}"