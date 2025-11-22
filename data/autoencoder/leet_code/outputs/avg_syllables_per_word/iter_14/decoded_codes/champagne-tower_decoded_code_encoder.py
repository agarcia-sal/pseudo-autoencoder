class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        current_row = [poured]
        for _ in range(query_row):
            next_row = [0.0] * (len(current_row) + 1)
            for i in range(len(current_row)):
                if current_row[i] > 1.0:
                    excess = (current_row[i] - 1.0) / 2.0
                    next_row[i] += excess
                    next_row[i + 1] += excess
            current_row = next_row
        return min(1.0, current_row[query_glass])