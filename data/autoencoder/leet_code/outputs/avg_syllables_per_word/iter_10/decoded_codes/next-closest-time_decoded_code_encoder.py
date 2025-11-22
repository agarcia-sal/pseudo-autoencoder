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
                            h = int(h1 + h2)
                            m = int(m1 + m2)
                            if h < 24 and m < 60:
                                times.append((h, m))
            return sorted(times)

        all_times = generate_times(digits)
        current_index = all_times.index((hour, minute))

        next_index = current_index + 1 if current_index + 1 < len(all_times) else 0
        next_hour, next_minute = all_times[next_index]

        return f"{next_hour:02d}:{next_minute:02d}"