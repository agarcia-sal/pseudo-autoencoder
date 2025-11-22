def is_pal(num):
    s = str(num)
    return s == s[::-1]

def gen_pal(limit):
    pals = []
    for i in range(1, 100000):
        s = str(i)
        pals.append(int(s + s[-2::-1]))
        pals.append(int(s + s[::-1]))
    return [p for p in pals if p <= limit]

def count_fair_and_square(left, right):
    L, R = int(left), int(right)
    limit = int(R**0.5) + 1

    pals = gen_pal(limit)
    count = 0
    for p in pals:
        sq = p * p
        if L <= sq <= R and is_pal(sq):
            count += 1
    return count