class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        position = {person: i for i, person in enumerate(row)}
        swaps = 0
        for i in range(0, len(row), 2):
            correct_pair = row[i] ^ 1  # the partner of row[i]
            if row[i + 1] != correct_pair:
                swap_index = position[correct_pair]
                row[i + 1], row[swap_index] = row[swap_index], row[i + 1]
                position[row[swap_index]] = swap_index
                position[row[i + 1]] = i + 1
                swaps += 1
        return swaps