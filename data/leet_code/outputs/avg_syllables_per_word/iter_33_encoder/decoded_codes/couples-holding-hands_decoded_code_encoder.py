class Solution:
    def minSwapsCouples(self, row):
        position = {}
        for i in range(len(row)):
            person = row[i]
            position[person] = i

        swaps = 0
        for i in range(0, len(row), 2):
            current_person = row[i]
            correct_pair = current_person + 1 if current_person % 2 == 0 else current_person - 1
            adjacent_person = row[i + 1]

            if adjacent_person != correct_pair:
                swap_idx = position[correct_pair]

                # Swap adjacent_person and correct_pair in row
                row[swap_idx], row[i + 1] = row[i + 1], row[swap_idx]

                # Update positions accordingly
                position[adjacent_person] = swap_idx
                position[correct_pair] = i + 1

                swaps += 1

        return swaps