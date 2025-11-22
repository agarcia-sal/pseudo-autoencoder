from collections import Counter

class Solution:
    def numRabbits(self, answers):
        answer_counts = Counter(answers)
        total_rabbits = 0
        for answer, count in answer_counts.items():
            groups = (count + answer) // (answer + 1)
            total_rabbits += groups * (answer + 1)
        return total_rabbits