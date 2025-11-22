from typing import List, Tuple

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7

        # Collect all unique y-coordinates
        y_coords = set()
        for x1, y1, x2, y2 in rectangles:
            y_coords.add(y1)
            y_coords.add(y2)
        y_coords = sorted(y_coords)

        # Map y-coordinate to index
        y_index = {y: i for i, y in enumerate(y_coords)}

        count = [0] * len(y_coords)
        events: List[Tuple[int, int, int, int]] = []

        # Create events for sweep line: add (eventType=1) or remove (eventType=-1)
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, 1, y1, y2))
            events.append((x2, -1, y1, y2))

        # Sort events by x coordinate
        events.sort(key=lambda e: e[0])

        prev_x = events[0][0] if events else 0
        area = 0

        for x, eventType, y1, y2 in events:
            # Calculate current covered length in y direction
            current_length = 0
            for i in range(1, len(y_coords)):
                if count[i-1] > 0:
                    current_length += y_coords[i] - y_coords[i-1]

            area += current_length * (x - prev_x)
            area %= MOD

            # Update count array based on event type
            start = y_index[y1]
            end = y_index[y2]
            for i in range(start, end):
                count[i] += eventType

            prev_x = x

        return area % MOD