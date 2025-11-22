def flipgame(fronts, backs):
    same = {x for x, y in zip(fronts, backs) if x == y}
    all_nums = set(fronts) | set(backs)
    good = all_nums - same
    return min(good) if good else 0