class Solution:
    def rectangleArea(self, rectangles):
        MODULO = 10**9 + 7

        unique_y_coordinates = set()
        for x1, y1, x2, y2 in rectangles:
            unique_y_coordinates.add(y1)
            unique_y_coordinates.add(y2)

        sorted_y_coordinates = sorted(unique_y_coordinates)

        y_index_mapping = {}
        for index in range(len(sorted_y_coordinates)):
            y_index_mapping[sorted_y_coordinates[index]] = index

        count_list = [0] * (len(sorted_y_coordinates) - 1)

        event_list = []
        for x1, y1, x2, y2 in rectangles:
            event_list.append((x1, 1, y1, y2))
            event_list.append((x2, -1, y1, y2))

        event_list.sort(key=lambda event: event[0])

        previous_x = 0
        total_area = 0

        for x, event_type, y1, y2 in event_list:
            active_length = 0
            for i in range(len(count_list)):
                if count_list[i] > 0:
                    active_length += sorted_y_coordinates[i + 1] - sorted_y_coordinates[i]

            segment_width = x - previous_x
            total_area += active_length * segment_width
            total_area %= MODULO

            start = y_index_mapping[y1]
            end = y_index_mapping[y2]
            if event_type == 1:
                for i in range(start, end):
                    count_list[i] += 1
            else:
                for i in range(start, end):
                    count_list[i] -= 1

            previous_x = x

        return total_area