from collections import defaultdict

class Solution:
    def largestOverlap(self, img1, img2):
        matrix_size = len(img1)
        list_of_points_one = []
        for row_index in range(matrix_size):
            for column_index in range(matrix_size):
                if img1[row_index][column_index] == 1:
                    list_of_points_one.append((row_index, column_index))

        list_of_points_two = []
        for row_index in range(matrix_size):
            for column_index in range(matrix_size):
                if img2[row_index][column_index] == 1:
                    list_of_points_two.append((row_index, column_index))

        dictionary_of_overlap_counts = defaultdict(int)
        for x1, y1 in list_of_points_one:
            for x2, y2 in list_of_points_two:
                delta_x = x2 - x1
                delta_y = y2 - y1
                dictionary_of_overlap_counts[(delta_x, delta_y)] += 1

        if not dictionary_of_overlap_counts:
            return 0
        return max(dictionary_of_overlap_counts.values())