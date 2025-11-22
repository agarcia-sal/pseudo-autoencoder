class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        current_row = [poured]
        for row in range(1, query_row + 1):
            next_row = [0] * (row + 1)
            for i in range(len(current_row)):
                if current_row[i] > 1:
                    excess = (current_row[i] - 1) / 2
                    next_row[i] += excess
                    next_row[i + 1] += excess
            current_row = next_row
        return current_row[query_glass] if current_row[query_glass] <= 1 else 1