def max_good_people(statements):
    n = len(statements)
    max_good = 0

    for mask in range(1 << n):
        good = [(mask & (1 << i)) != 0 for i in range(n)]
        valid = True

        for i in range(n):
            if good[i]:
                for j in range(n):
                    if (statements[i][j] == 0 and good[j]) or (statements[i][j] == 1 and not good[j]):
                        valid = False
                        break
                if not valid:
                    break

        if valid:
            max_good = max(max_good, sum(good))

    return max_good