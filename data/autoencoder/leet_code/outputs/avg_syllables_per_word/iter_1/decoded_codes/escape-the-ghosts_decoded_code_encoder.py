def escape_possible(ghosts, target_x, target_y):
    p = abs(target_x) + abs(target_y)
    for g_x, g_y in ghosts:
        if abs(g_x - target_x) + abs(g_y - target_y) <= p:
            return False
    return True