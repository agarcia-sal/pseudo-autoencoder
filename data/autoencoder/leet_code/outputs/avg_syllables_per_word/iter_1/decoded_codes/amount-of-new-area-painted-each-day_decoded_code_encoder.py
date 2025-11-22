def paint_worklog(paint):
    max_end = max(end for _, end in paint)
    painted = [-1] * (max_end + 1)
    worklog = []

    for start, end in paint:
        cur = start
        new = 0
        while cur < end:
            if painted[cur] == -1:
                painted[cur] = end
                new += 1
                cur += 1
            else:
                cur = painted[cur]
        worklog.append(new)

    return worklog