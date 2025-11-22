import heapq

def schedule_courses(courses):
    courses.sort(key=lambda x: x[1])  # sort by end day
    max_heap = []
    current_end_day = 0

    for d, e in courses:
        if current_end_day + d <= e:
            heapq.heappush(max_heap, -d)
            current_end_day += d
        elif max_heap and -max_heap[0] > d:
            current_end_day += d + heapq.heappop(max_heap)
            heapq.heappush(max_heap, -d)

    return len(max_heap)