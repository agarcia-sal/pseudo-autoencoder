class Solution:
    def matrixScore(self, grid):
        for row in grid:
            if row[0] == 0:
                for i in range(len(row)):
                    row[i] = 1 - row[i]

        for col in range(1, len(grid[0])):
            count_ones = 0
            for row in grid:
                count_ones += row[col]
            if count_ones < len(grid) / 2:
                for row in grid:
                    row[col] = 1 - row[col]

        total_score = 0
        for row in grid:
            total_score += self.binaryListToInteger(row)
        return total_score

    def binaryListToInteger(self, binary_list):
        # Convert list of binary digits to integer
        result = 0
        for bit in binary_list:
            result = (result << 1) | bit
        return result