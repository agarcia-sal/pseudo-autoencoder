class Solution:
    def rectangleArea(self, rectangles):
        MOD = 10**9 + 7
        y_coords = set()
        for rect in rectangles:
            x1, y1, x2, y2 = rect
            y_coords.add(y1)
            y_coords.add(y2)
        y_coords = sorted(y_coords)
        y_index = {y: i for i, y in enumerate(y_coords)}
        count = [0] * len(y_coords)
        events = []
        for rect in rectangles:
            x1, y1, x2, y2 = rect
            events.append((x1, 1, y1, y2))
            events.append((x2, -1, y1, y2))
        events.sort(key=lambda e: e[0])
        prev_x = 0
        area = 0
        for x, eventType, y1, y2 in events:
            current_length = 0
            for i in range(1, len(y_coords)):
                if count[i - 1] > 0:
                    current_length += y_coords[i] - y_coords[i - 1]
            area += current_length * (x - prev_x)
            area %= MOD
            idx_start = y_index[y1]
            idx_end = y_index[y2]
            if eventType == 1:
                for i in range(idx_start, idx_end):
                    count[i] += 1
            else:
                for i in range(idx_start, idx_end):
                    count[i] -= 1
            prev_x = x
        return area