def matrix_score(grid):
    rows, cols = len(grid), len(grid[0])

    # Flip rows where first element is 0
    for r in range(rows):
        if grid[r][0] == 0:
            grid[r] = [1 - bit for bit in grid[r]]

    # Flip columns where count of 1s is less than half of rows
    for c in range(1, cols):
        count_ones = sum(grid[r][c] for r in range(rows))
        if count_ones < rows / 2:
            for r in range(rows):
                grid[r][c] = 1 - grid[r][c]

    # Calculate score by interpreting each row as binary number
    score = 0
    for r in range(rows):
        # Convert row bits to string and then to int base 2
        binary_str = ''.join(str(bit) for bit in grid[r])
        score += int(binary_str, 2)

    return score