class Solution:
    def minSwapsCouples(self, row):
        position = {}
        for i in range(len(row)):
            person = row[i]
            position[person] = i

        swaps = 0
        for i in range(0, len(row), 2):
            person = row[i]
            correct_pair = person + 1 if person % 2 == 0 else person - 1
            if row[i + 1] != correct_pair:
                swap_idx = position[correct_pair]
                # Swap the persons at i+1 and swap_idx
                row[i + 1], row[swap_idx] = row[swap_idx], row[i + 1]
                # Update their positions
                position[row[swap_idx]] = swap_idx
                position[row[i + 1]] = i + 1
                swaps += 1
        return swaps