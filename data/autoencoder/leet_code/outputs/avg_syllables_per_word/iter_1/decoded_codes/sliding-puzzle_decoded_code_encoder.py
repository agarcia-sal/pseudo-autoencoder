from collections import deque

def sliding_puzzle(board):
    start = tuple(tuple(row) for row in board)
    target = ((1, 2, 3), (4, 5, 0))
    neighbors = {0: {1, 3}, 1: {0, 2, 4}, 2: {1, 5}, 3: {0, 4}, 4: {1, 3, 5}, 5: {2, 4}}

    # Find the index of zero in the flattened board
    zero_pos = next(i for i, v in enumerate(sum(start, ())) if v == 0)

    queue = deque([(start, zero_pos, 0)])
    visited = {start}

    while queue:
        state, zero, moves = queue.popleft()
        if state == target:
            return moves
        # Convert zero_pos to 2D indices
        r1, c1 = divmod(zero, 3)
        for n in neighbors[zero]:
            r2, c2 = divmod(n, 3)
            new_state = [list(row) for row in state]
            # Swap zero and neighbor positions
            new_state[r1][c1], new_state[r2][c2] = new_state[r2][c2], new_state[r1][c1]
            new_tuple = tuple(tuple(row) for row in new_state)
            if new_tuple not in visited:
                visited.add(new_tuple)
                queue.append((new_tuple, n, moves + 1))

    return -1