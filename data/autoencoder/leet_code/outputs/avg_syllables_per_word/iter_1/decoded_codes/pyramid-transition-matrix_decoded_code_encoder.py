from collections import defaultdict

map = defaultdict(list)
for rule in allowed:
    map[rule[0], rule[1]].append(rule[2])

def build(bottom, top):
    if len(bottom) == 1:
        return True
    if len(top) == len(bottom) - 1:
        return build(top, "")
    L, R = bottom[len(top)], bottom[len(top) + 1]
    for t in map[L, R]:
        if build(bottom, top + t):
            return True
    return False

return build(bottom, "")