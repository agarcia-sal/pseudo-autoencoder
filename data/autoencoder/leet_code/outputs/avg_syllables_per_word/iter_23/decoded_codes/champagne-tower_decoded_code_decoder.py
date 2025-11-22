from typing import List

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        current_row = [poured]
        for _ in range(query_row):
            next_row = [0.0] * (len(current_row) + 1)
            for i, amount in enumerate(current_row):
                if amount > 1.0:
                    excess = (amount - 1.0) / 2.0
                    next_row[i] += excess
                    next_row[i + 1] += excess
            current_row = next_row
        return min(1.0, current_row[query_glass])