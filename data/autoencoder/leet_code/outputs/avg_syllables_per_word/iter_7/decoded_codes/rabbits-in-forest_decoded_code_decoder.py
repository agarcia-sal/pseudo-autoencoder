from collections import Counter
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answer_counts = Counter(answers)
        total_rabbits = 0
        for answer, count in answer_counts.items():
            groups = (count + answer) // (answer + 1)
            total_rabbits += groups * (answer + 1)
        return total_rabbits