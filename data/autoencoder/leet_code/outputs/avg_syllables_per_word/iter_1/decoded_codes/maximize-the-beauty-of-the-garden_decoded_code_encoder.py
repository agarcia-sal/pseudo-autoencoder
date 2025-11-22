def max_beauty(flowers):
    from collections import defaultdict

    idxs = defaultdict(list)
    prefix = [0] * (len(flowers) + 1)

    for i in range(len(flowers)):
        prefix[i + 1] = prefix[i] + max(flowers[i], 0)
        idxs[flowers[i]].append(i)

    max_b = float('-inf')
    for b in idxs:
        if len(idxs[b]) >= 2:
            f, l = idxs[b][0], idxs[b][-1]
            val = 2 * b + prefix[l] - prefix[f + 1]
            max_b = max(max_b, val)

    return max_b