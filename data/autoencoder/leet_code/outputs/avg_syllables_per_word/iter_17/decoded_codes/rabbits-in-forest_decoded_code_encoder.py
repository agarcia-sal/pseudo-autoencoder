from collections import Counter
from typing import List

class Solution:
    def numRabbits(self, list_of_answers: List[int]) -> int:
        answer_counts = Counter(list_of_answers)
        total_rabbits = 0
        for answer, count in answer_counts.items():
            group_size = answer + 1
            groups = (count + answer) // group_size
            total_rabbits += groups * group_size
        return total_rabbits