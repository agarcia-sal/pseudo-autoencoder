class Solution:
    def minSwapsCouples(self, row):
        position = {}
        # Map each person to their current index
        for i in range(0, len(row), 2):
            position[row[i]] = i
            position[row[i + 1]] = i + 1

        swaps = 0
        for i in range(0, len(row), 2):
            correct_pair = row[i] ^ 1
            if row[i + 1] != correct_pair:
                swap_idx = position[correct_pair]

                # Swap the persons in the row
                row[i + 1], row[swap_idx] = row[swap_idx], row[i + 1]

                # Update positions in the dictionary accordingly
                position[row[swap_idx]] = swap_idx
                position[row[i + 1]] = i + 1

                swaps += 1

        return swaps