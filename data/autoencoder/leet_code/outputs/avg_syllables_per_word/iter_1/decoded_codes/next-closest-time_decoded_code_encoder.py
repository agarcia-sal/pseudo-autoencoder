def next_closest_time(time: str) -> str:
    digits = set(time.replace(":", ""))
    hour, minute = map(int, time.split(":"))

    def gen_times(digits):
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

    all_times = gen_times(digits)
    idx = all_times.index((hour, minute))

    if idx + 1 < len(all_times):
        next_h, next_m = all_times[idx + 1]
    else:
        next_h, next_m = all_times[0]

    return "{:02}:{:02}".format(next_h, next_m)