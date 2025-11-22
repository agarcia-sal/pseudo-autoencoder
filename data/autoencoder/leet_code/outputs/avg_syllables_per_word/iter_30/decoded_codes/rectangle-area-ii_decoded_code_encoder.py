class Solution:
    def rectangleArea(self, rectangles):
        MODULO = 10**9 + 7

        y_coordinates = set()
        for x1, y1, x2, y2 in rectangles:
            y_coordinates.add(y1)
            y_coordinates.add(y2)
        y_coordinates = sorted(y_coordinates)

        y_index = {y: i for i, y in enumerate(y_coordinates)}
        count = [0] * len(y_coordinates)

        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, 1, y1, y2))
            events.append((x2, -1, y1, y2))
        events.sort(key=lambda e: e[0])

        previous_x = 0
        area = 0

        for x, eventType, y1, y2 in events:
            current_length = 0
            for i in range(1, len(count)):
                if count[i - 1] > 0:
                    current_length += y_coordinates[i] - y_coordinates[i - 1]

            area += current_length * (x - previous_x)
            area %= MODULO

            start = y_index[y1]
            end = y_index[y2]
            delta = 1 if eventType == 1 else -1
            for i in range(start, end):
                count[i] += delta

            previous_x = x

        return area