from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7

        y_coords = set()
        for rectangle in rectangles:
            x1, y1, x2, y2 = rectangle
            y_coords.add(y1)
            y_coords.add(y2)

        y_coords = sorted(y_coords)

        def create_y_index(y_coords):
            y_index = {}
            for i, y in enumerate(y_coords):
                y_index[y] = i
            return y_index

        y_index = create_y_index(y_coords)

        def create_count_list(length):
            return [0] * length

        count = create_count_list(len(y_coords))

        events = []
        for rectangle in rectangles:
            x1, y1, x2, y2 = rectangle
            events.append((x1, 1, y1, y2))
            events.append((x2, -1, y1, y2))

        def sort_events(events):
            events.sort(key=lambda e: e[0])
            return events

        events = sort_events(events)

        prev_x = 0
        area = 0

        for x, eventType, y1, y2 in events:
            current_length = 0
            for i in range(1, len(count)):
                if count[i - 1] > 0:
                    current_length += y_coords[i] - y_coords[i - 1]

            area += current_length * (x - prev_x)
            area %= MOD

            start = y_index[y1]
            end = y_index[y2]
            for i in range(start, end):
                count[i] += eventType

            prev_x = x

        return area % MOD