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

        # Map each y coordinate to its index
        y_index = {v: i for i, v in enumerate(y_coords)}

        # Count array to track active segments between y-coordinates
        count = [0] * len(y_coords)

        # Create event list: (x, type, y1, y2)
        # type: 1 for rectangle start, -1 for rectangle end
        events: List[Tuple[int,int,int,int]] = []
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, 1, y1, y2))
            events.append((x2, -1, y1, y2))

        # Sort events by x-coordinate
        events.sort(key=lambda e: e[0])

        prev_x = 0
        area = 0

        for x, eventType, y1, y2 in events:
            # Calculate the vertical coverage length at prev_x
            current_length = 0
            for i in range(1, len(y_coords)):
                if count[i - 1] > 0:
                    current_length += y_coords[i] - y_coords[i - 1]

            # Add the area covered since last x to current x
            area += current_length * (x - prev_x)
            area %= MOD

            # Update count according to event type over y-interval
            start = y_index[y1]
            end = y_index[y2]
            if eventType == 1:
                for i in range(start, end):
                    count[i] += 1
            else:
                for i in range(start, end):
                    count[i] -= 1

            prev_x = x

        return area % MOD