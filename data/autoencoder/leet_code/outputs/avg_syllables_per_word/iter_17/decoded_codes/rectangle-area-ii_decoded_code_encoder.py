from bisect import bisect_left

class Solution:
    def rectangleArea(self, rectangles):
        MOD = 10**9 + 7

        y_coords = set()
        for x1, y1, x2, y2 in rectangles:
            y_coords.add(y1)
            y_coords.add(y2)

        y_coords = sorted(y_coords)
        y_index = self.CreateIndexMapping(y_coords)
        count = self.InitializeCountList(len(y_coords))

        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, 1, y1, y2))
            events.append((x2, -1, y1, y2))

        events.sort()

        prev_x = 0
        area = 0

        for x, eventType, y1, y2 in events:
            current_length = 0
            for i in range(1, len(count)):
                if count[i - 1] > 0:
                    current_length += y_coords[i] - y_coords[i - 1]

            area += current_length * (x - prev_x)
            area %= MOD

            start_idx = y_index[y1]
            end_idx = y_index[y2]
            if eventType == 1:
                for i in range(start_idx, end_idx):
                    count[i] += 1
            else:
                for i in range(start_idx, end_idx):
                    count[i] -= 1

            prev_x = x

        return area

    def CreateIndexMapping(self, list_of_values):
        # Create a dictionary mapping each value to its index
        return {value: idx for idx, value in enumerate(list_of_values)}

    def InitializeCountList(self, length_of_list):
        # Initialize a list of zeroes for counts (length_of_list - 1 ranges)
        return [0] * (length_of_list - 1)