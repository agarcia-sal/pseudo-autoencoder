class Solution:
    def minSwapsCouples(self, row):
        position = {person: idx for idx, person in enumerate(row)}
        swaps = 0
        for i in range(0, len(row), 2):
            correct_pair = row[i] ^ 1
            if row[i + 1] != correct_pair:
                swap_idx = position[correct_pair]

                # swap the two people
                row[i + 1], row[swap_idx] = row[swap_idx], row[i + 1]

                # update positions after swap
                position[row[swap_idx]] = swap_idx
                position[row[i + 1]] = i + 1

                swaps += 1
        return swaps