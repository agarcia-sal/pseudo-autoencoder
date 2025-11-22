from typing import List

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        current_row: List[float] = [float(poured)]
        for row in range(1, query_row + 1):
            next_row = [0.0] * (row + 1)
            for i in range(len(current_row)):
                if current_row[i] > 1.0:
                    excess = (current_row[i] - 1.0) / 2.0
                    next_row[i] += excess
                    next_row[i + 1] += excess
            current_row = next_row
        return current_row[query_glass] if current_row[query_glass] < 1.0 else 1.0