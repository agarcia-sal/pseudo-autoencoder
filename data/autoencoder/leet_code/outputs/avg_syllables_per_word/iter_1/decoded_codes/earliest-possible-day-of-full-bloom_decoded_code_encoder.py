def earliest_full_bloom(tasks):
    tasks.sort(key=lambda x: x[1], reverse=True)
    cur_day, earliest = 0, 0
    for plant, grow in tasks:
        cur_day += plant
        earliest = max(earliest, cur_day + grow)
    return earliest