def shortest_distance(wordsDict, word1, word2):
    min_dist = float('inf')
    p1 = -1
    p2 = -1
    same = (word1 == word2)

    for i, w in enumerate(wordsDict):
        if w == word1:
            if same:
                p2 = p1
            p1 = i
        if w == word2 and not same:
            p2 = i
        if p1 != -1 and p2 != -1:
            min_dist = min(min_dist, abs(p1 - p2))

    return min_dist