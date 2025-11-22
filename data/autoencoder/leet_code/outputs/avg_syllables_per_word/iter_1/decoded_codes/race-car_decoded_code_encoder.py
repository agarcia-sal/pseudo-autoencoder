from collections import deque

def racecar(target):
    queue = deque([(0, 1, 0)])  # (pos, spd, steps)
    visited = set([(0, 1)])

    while queue:
        pos, spd, steps = queue.popleft()
        if pos == target:
            return steps

        next_pos, next_spd = pos + spd, spd * 2
        if 0 <= next_pos < 2 * target and (next_pos, next_spd) not in visited:
            visited.add((next_pos, next_spd))
            queue.append((next_pos, next_spd, steps + 1))

        next_spd = -1 if spd > 0 else 1
        if 0 <= pos < 2 * target and (pos, next_spd) not in visited:
            visited.add((pos, next_spd))
            queue.append((pos, next_spd, steps + 1))