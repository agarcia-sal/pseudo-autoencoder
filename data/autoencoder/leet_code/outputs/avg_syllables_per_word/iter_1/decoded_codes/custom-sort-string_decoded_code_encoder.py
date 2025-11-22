def sort_by_order(s, order):
    d = {c: i for i, c in enumerate(order)}
    return ''.join(sorted(s, key=lambda x: d.get(x, 0)))