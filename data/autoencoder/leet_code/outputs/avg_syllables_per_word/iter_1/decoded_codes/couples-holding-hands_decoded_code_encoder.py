def min_swaps_couples(row):
    pos = {person: i for i, person in enumerate(row)}
    swaps = 0
    for i in range(0, len(row), 2):
        pair = row[i] ^ 1
        if row[i + 1] != pair:
            j = pos[pair]
            row[i + 1], row[j] = row[j], row[i + 1]
            pos[row[j]] = j
            pos[row[i + 1]] = i + 1
            swaps += 1
    return swaps