from collections import Counter
from math import ceil

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        answer_counts = Counter(answers)
        total_rabbits = 0
        for answer, count in answer_counts.items():
            group_size = answer + 1
            groups = ceil(count / group_size)
            total_rabbits += groups * group_size
        return total_rabbits