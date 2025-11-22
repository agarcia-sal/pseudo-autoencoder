from itertools import product

class Solution:
    def countCombinations(self, list_of_pieces, list_of_positions):
        directions = {
            'rook': [(1, 0), (-1, 0), (0, 1), (0, -1)],
            'queen': [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)],
            'bishop': [(1, 1), (-1, 1), (1, -1), (-1, -1)],
        }

        # Adjust input positions from 1-based to 0-based indexing
        list_of_positions = [(row - 1, col - 1) for row, col in list_of_positions]

        def get_destinations(start_position, piece_type):
            row, column = start_position
            destinations = [start_position]
            for delta_row, delta_column in directions[piece_type]:
                new_row = row + delta_row
                new_column = column + delta_column
                while 0 <= new_row < 8 and 0 <= new_column < 8:
                    destinations.append((new_row, new_column))
                    new_row += delta_row
                    new_column += delta_column
            return destinations

        all_destinations = [get_destinations(pos, piece) for pos, piece in zip(list_of_positions, list_of_pieces)]

        def is_valid_combination(candidate_combination):
            current_positions = list(list_of_positions)
            number_of_pieces = len(current_positions)
            while True:
                if len(set(current_positions)) < number_of_pieces:
                    return False
                all_pieces_reached = True
                for i in range(number_of_pieces):
                    if current_positions[i] == candidate_combination[i]:
                        continue
                    all_pieces_reached = False
                    current_row, current_column = current_positions[i]
                    target_row, target_column = candidate_combination[i]

                    if target_row > current_row:
                        delta_row = 1
                    elif target_row < current_row:
                        delta_row = -1
                    else:
                        delta_row = 0

                    if target_column > current_column:
                        delta_column = 1
                    elif target_column < current_column:
                        delta_column = -1
                    else:
                        delta_column = 0

                    current_positions[i] = (current_row + delta_row, current_column + delta_column)
                if all_pieces_reached:
                    return True

        valid_count = 0
        for combination in product(*all_destinations):
            if is_valid_combination(combination):
                valid_count += 1

        return valid_count