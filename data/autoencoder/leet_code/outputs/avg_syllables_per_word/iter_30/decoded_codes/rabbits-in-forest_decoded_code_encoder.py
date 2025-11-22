from collections import Counter

class Solution:
    def numRabbits(self, answers):
        answer_counts = Counter(answers)
        total_rabbits = 0
        for answer, count in answer_counts.items():
            group_size = answer + 1
            groups = (count + answer) // group_size
            total_rabbits += groups * group_size
        return total_rabbits