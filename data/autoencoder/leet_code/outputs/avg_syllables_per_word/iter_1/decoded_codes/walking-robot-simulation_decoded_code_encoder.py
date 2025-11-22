def robotSim(commands, obstacles):
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    x = y = dir_i = max_d = 0
    obs = set(tuple(o) for o in obstacles)
    for c in commands:
        if c == -2:
            dir_i = (dir_i - 1) % 4
        elif c == -1:
            dir_i = (dir_i + 1) % 4
        else:
            dx, dy = dirs[dir_i]
            for _ in range(c):
                nx, ny = x + dx, y + dy
                if (nx, ny) in obs:
                    break
                x, y = nx, ny
            max_d = max(max_d, x*x + y*y)
    return max_d