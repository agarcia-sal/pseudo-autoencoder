class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        position = {}
        for idx, person in enumerate(row):
            position[person] = idx
        swaps = 0
        for i in range(0, len(row), 2):
            correct_pair = row[i] ^ 1
            if row[i + 1] != correct_pair:
                swap_idx = position[correct_pair]
                temp = row[i + 1]
                row[i + 1] = row[swap_idx]
                row[swap_idx] = temp
                position[row[swap_idx]] = swap_idx
                position[row[i + 1]] = i + 1
                swaps += 1
        return swaps