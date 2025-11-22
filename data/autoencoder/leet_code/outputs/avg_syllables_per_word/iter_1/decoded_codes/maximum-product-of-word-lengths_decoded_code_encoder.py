def max_product(words):
    sets = [set(word) for word in words]
    max_product = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if sets[i].isdisjoint(sets[j]):
                max_product = max(max_product, len(words[i]) * len(words[j]))
    return max_product