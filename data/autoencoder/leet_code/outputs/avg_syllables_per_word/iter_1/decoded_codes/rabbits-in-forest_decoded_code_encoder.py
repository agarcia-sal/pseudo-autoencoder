from collections import Counter

def calculate_total(answers):
    count = Counter(answers)
    total = 0
    for a, c in count.items():
        groups = (c + a) // (a + 1)
        total += groups * (a + 1)
    return total